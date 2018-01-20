import numpy as np

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

# MOOD_RANGES = {
#     'positive': {
#         (1.75, 2.25): 'up',
#         (1.25, 1.75): 'middle',
#         (0.75, 1.25): 'down'
#     },
#     'neutral': {
#         (0.25, 0.75): 'up',
#         (-0.25, 0.25): 'middle',
#         (-0.75, -0.25): 'down'
#     },
#     'negative': {
#         (-1.25, -0.75): 'up',
#         (-1.75, -1.25): 'middle',
#         (-2.25, -1.75): 'down'
#     }
# }

MOOD_AVERAGES = {
    ('negative', 'down'): -2,
    ('negative', 'middle'): -1.5,
    ('negative', 'up'): -1,
    ('neutral', 'down'): -0.5,
    ('neutral', 'middle'): -0.25,
    ('neutral', 'middle'): 0.0,
    ('neutral', 'up'): 0.5,
    ('positive', 'down'): 1,
    ('positive', 'middle'): 1.5,
    ('positive', 'up'): 2

}
