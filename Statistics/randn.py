import random
from random import seed


# declaring list
def randn(n):
    list = []

    # initializing the value of n
    random.seed(1)
    # traversing and printing random elements
    for i in range(n):
        result = random.choice(list)
        return result
