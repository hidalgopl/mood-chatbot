from django.core.cache import cache
from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from nlp.constants import VERIFY_TOKEN
from nlp.services import MessageAnalyzer

from .services import send_text_message


def verify_fb_token(token_sent, request):
    if token_sent == VERIFY_TOKEN:
        return HttpResponse(request.GET.get("hub.challenge"))
    return Response(data={'info': 'Verification token is invalid.'}, status=400)


@api_view(['GET', 'POST'])
def webhook(request):
    if request.method == 'GET':
        token_sent = request.GET.get("hub.verify_token")
        return verify_fb_token(token_sent, request)
    else:
        output = request.data
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    message_text = message['message'].get('text')
                    if message_text:
                        last_mood = cache.get(recipient_id, 0)
                        m = MessageAnalyzer(message=message_text, last_mood=last_mood)
                        response_sent_text, current_mood = m.analyze()
                        send_text_message(recipient_id, response_sent_text)
                        # store bot current mood in this conversation in cache.
                        cache.set(recipient_id, current_mood)
        return Response(status=200)
