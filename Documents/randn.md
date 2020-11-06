#Select N number of items from a list without a seed

Random Module:
Random module is the predefined Module in Python, It contains methods to return random values. This module is useful when we want to generate random values. Some of the methods of Random module are:-
seed(), getstate(), choice(), sample() etc.

Example:

    import random 
  

    list = [2, 2, 4, 6, 6, 8] 
    n = 4
    for i in range(n): 
        print(random.choice(list), end = " ") 
        
Output:

    8 2 4 6