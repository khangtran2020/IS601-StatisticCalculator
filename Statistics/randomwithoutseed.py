import random
from random import randint

value = randint(0, 10)
print("The random integer between 0 and 10 is :", value)
print("The random floating point number between 5 and 10 is : ", end="")
print(random.uniform(5, 10))
