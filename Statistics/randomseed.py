# generate random integer values
import random
from random import seed
from random import randint

# seed random number generator
seed(1)


# generate some integers

def seedint(a, b):
    value = randint(a, b)
    return value


def seedfloat(a, b):
    value = random.uniform(a, b)
    return value
