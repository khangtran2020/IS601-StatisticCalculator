import random
from random import seed


def Rand(start, end, num):
    res = []
    seed(1)
    for j in range(num):
        res.append(random.randint(start, end))

    return res
