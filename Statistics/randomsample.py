import random


def randsample(data, n):
    result = []
    random.seed(1)
    result = random.sample(data, n)
    return result
