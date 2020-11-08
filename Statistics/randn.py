import random
from random import seed


# declaring list
def randn(data, n):
    list = []
    random.seed(1)
    for i in range(n):
        list.append(random.choice(data))
    return list
