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
        'up': ["That's fabulous!", "Oh great!", 'Amazing!'],
        'middle': ["Oh, that's really nice!", "Glad to hear it:)", "Sounds good"],
        'down': ["It's not so bad", "Always look on the bright side of life", ]
    },
    'negative': {
        'up': ["I hate it more than anything!", "I'm so upset I will explode"],
        'middle': ["I don't like it at all", "I expected better answer."],
        'down': ["That's really bad", "Not good."]
    },
    'neutral': {
        'up': ["Let's change the topic"],
        'middle': ["It's ok", "No problem"],
        'down': ["Ok, I can accept this."]
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
