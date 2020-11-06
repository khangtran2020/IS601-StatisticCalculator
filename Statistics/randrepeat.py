import random


def randrepeat(start, end):
    for i in range(start, end):
        # Any number can be used in place of '0'.
        random.seed(0)

        # Generated random number will be between the given range.
        result = random.randint(start, end)
        return result
