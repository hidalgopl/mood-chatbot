MOOD_MAP = {
    'joy': 'positive',
    'confident': 'neutral',
    'sadness': 'negative',
    'anger': 'negative',
    'fear': 'negative',
    'analytical': 'neutral',
    'tentative': 'neutral'
}

RESPONSES = {
    # feel free to add more responses
    'positive': {
        'up': ["That's fabulous!", "Oh great!", 'Amazing!', "Wow I'm really impressed!", "A W E S O M E"],
        'middle': ["Oh, that's really nice!", "Glad to hear it:)", "Sounds good", "That's good:)", "Wicked!"],
        'down': ["It's not so bad", "Always look on the bright side of life", "It could be much worse", "It will be better", "Not too bad"]
    },
    'negative': {
        'up': ["I hate it more than anything!", "I'm so upset I will explode", "I'm disgusted.", "It's horrible.", "It's terrible"],
        'middle': ["I don't like it at all", "I expected better answer.", "I'm scared.", "Why you do this? :((", "Please don't go this way."],
        'down': ["That's really bad", "Not good.", "I'm not happy with that.", "This is not something I would like to hear", "I'm frustrated."]
    },
    'neutral': {
        'up': ["Let's change the topic", "Can we talk about something different?:)", "Roger that", "OK - I understand", "No problem mate:)"],
        'middle': ["It's ok", "No problem", "OK", "That's not a big deal", "Cool"],
        'down': ["Ok, I can accept this.", "Ehh.. I understand your point of view.", "I must accept that.", "Maybe next time it will be better", "Sure..."]
    }
}
MOOD_AVERAGES = {
    ('negative', 'down'): -2,
    ('negative', 'middle'): -1.5,
    ('negative', 'up'): -1,
    ('neutral', 'down'): -0.5,
    ('neutral', 'middle'): 0.0,
    ('neutral', 'up'): 0.5,
    ('positive', 'down'): 1,
    ('positive', 'middle'): 1.5,
    ('positive', 'up'): 2

}
