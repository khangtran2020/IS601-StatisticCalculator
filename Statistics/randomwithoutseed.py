import random
from random import randint


def noseedint(a, b):
    value = randint(a, b)
    return value


def noseedfloat(a, b):
    value = random.uniform(a, b)
    return value
