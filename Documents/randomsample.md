#Simple random sampling

Python’s random module provides random.sample() function for random sampling and randomly pick more than one element from the list without repeating elements. The random.sample() returns a list of unique elements chosen randomly from the list, sequence, or set, we call it random sampling without replacement.

In simple terms, for example, you have a list of 100 names, and you want to choose ten names randomly from it without repeating names, then you must use random.sample().

Example:

    import random

    aList = [20, 40, 80, 100, 120]
    print ("choosing 3 random items from a list using random.sample() function")
    sampled_list = random.sample(aList, 3)
    print(sampled_list)
    
Output:

    choosing 3 random items from a list using random.sample() function
    [40, 120, 100]