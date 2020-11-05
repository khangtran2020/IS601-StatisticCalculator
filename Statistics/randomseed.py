# generate random integer values
import random
from random import seed
from random import randint

# seed random number generator



# generate some integers

def seedint(a, b):
    seed(1)
    value = randint(a, b)
    return value


def seedfloat(a, b):
    seed(1)
    value = random.uniform(a, b)
    return value
