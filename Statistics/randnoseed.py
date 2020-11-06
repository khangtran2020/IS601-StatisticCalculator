import random
from random import seed


# declaring list
def randn(n):
    list1 = []

    # initializing the value of n
    seed(1)
    # traversing and printing random elements
    for i in range(n):
        result = random.choice(list1)
        return result
