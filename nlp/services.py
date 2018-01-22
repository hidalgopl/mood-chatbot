import random

from watson_developer_cloud.tone_analyzer_v3 import ToneAnalyzerV3

from .generics import MOOD_AVERAGES, MOOD_MAP, RESPONSES


class MessageAnalyzer:
    def __init__(self, message, last_mood=0):
        # last mood is the bot mood after the last user's response.
        # If it's begin of conversation, bot's mood is neutral.
        self.message = message
        self.tone_analyzer = ToneAnalyzerV3(
            # TODO if I have more time:
            # these keys should be separated to ENV variables
            version='2017-09-21',
            username='17b5c766-76dc-4225-8339-c4a6e84b72c8',
            password='rOxKKOHUPcZS'
        )
        self.mood = last_mood

    @staticmethod
    def get_mood_rate(mood, tier):
        return MOOD_AVERAGES[(mood, tier)]

    @staticmethod
    def get_mood_from_rate(rate):
        if rate < -0.75:
            mood = 'negative'
            if -1.25 <= rate < -0.75:
                return mood, 'up'
            elif -1.75 <= rate < -1.25:
                return mood, 'middle'
            else:
                return mood, 'down'
        elif -0.75 <= rate < 0.75:
            mood = 'neutral'
            if -0.75 <= rate < -0.25:
                return mood, 'down'
            elif -0.25 <= rate < 0.25:
                return mood, 'middle'
            else:
                return mood, 'up'
        elif 0.75 <= rate:
            mood = 'positive'
            if 0.75 <= rate < 1.25:
                return mood, 'down'
            elif 1.25 <= rate < 1.75:
                return mood, 'middle'
            else:
                return mood, 'up'

    @staticmethod
    def get_message_main_tone(tones_list):
        # create a list of all tones in the user's message
        all_tones = [d['tone_id'] for d in tones_list]
        if 'sadness' in all_tones:
            # if one of the tones of user's message is sad, fear or anger, message is negative.
            return list(filter(lambda d: d['tone_id'] == 'sadness', tones_list))[0]
        elif 'fear' in all_tones:
            return list(filter(lambda d: d['tone_id'] == 'tone_id', tones_list))[0]
        elif 'anger' in all_tones:
            return list(filter(lambda d: d['tone_id'] == 'anger', tones_list))[0]
        elif 'joy' in all_tones:
            return list(filter(lambda d: d['tone_id'] == 'joy', tones_list))[0]
        else:
            try:
                # get a tone with highest score
                return sorted(tones_list, key=lambda d: d['score'], reverse=True)[0]
            except IndexError:
                # by default, all bots are happy!
                return {'tone_id': 'joy', 'score': 0.88}

    @staticmethod
    def get_mood(tone):
        return MOOD_MAP[tone]

    def get_text_mood_and_score(self, tone):
        mood = self.get_mood(tone['tone_id'])
        return mood, tone['score']

    def analyze(self):
        if self.message.lower() == 'mood':
            # requirement: magic message "mood" returns current bot's mood
            return '{}'.format(self.get_mood_from_rate(self.mood)[0]), self.mood
        response = self.tone_analyzer.tone(self.message, content_type='text/plain')
        tone = self.get_message_main_tone(response['document_tone']['tones'])
        mood, score = self.get_text_mood_and_score(tone)
        tier = self.get_mood_tier(score)
        self.mood += self.get_mood_rate(mood, tier)
        message = self.get_generic_response(*self.get_mood_from_rate(self.mood))
        return message, self.mood

    @staticmethod
    def get_generic_response(mood, tier):
        responses_list = RESPONSES[mood][tier]
        return "(mood {} - {}) {}".format(
            tier, mood, random.choice(responses_list)
        )

    @staticmethod
    def get_mood_tier(score):
        # IBM Watson Tone Analyzer returns only the tones that have score greater than or equal 0.5
        # that's the most obvious 3 tiers between 0.5 and 1.0
        if score >= 0.83:
            return 'up'
        elif score >= 0.66:
            return 'middle'
        else:
            return 'down'
