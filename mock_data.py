import random

def external_scores():
    return {
        "0x0000000000000000000000000000000000000001": random.randint(0, 100),
        "0x0000000000000000000000000000000000000002": random.randint(0, 100),
    }
