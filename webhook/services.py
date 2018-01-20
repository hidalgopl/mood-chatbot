import requests
from django.conf import settings

from .constants import ACCESS_TOKEN


def send_text_message(recipient_id, text):
    url = settings.MESSENGER_WEBHOOK_URL.format(ACCESS_TOKEN)
    data = {
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": text
        }
    }
    sent = requests.post(url, json=data)
