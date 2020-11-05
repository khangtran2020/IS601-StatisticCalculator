# Generate a list of N random numbers with a seed and between a range of numbers 

Given lower and upper limits, generate a given count of random numbers within a given range, starting from ‘start’ to ‘end’ and store them in list.

Examples:

    Input : num = 10, start = 20, end = 40
    Output : [23, 20, 30, 33, 30, 36, 37, 27, 28, 38]
    The output contains 10 random numbers in
    range [20, 40].

    Input : num = 5, start = 10, end = 15
    Output : [15, 11, 15, 12, 11]
    The output contains 5 random numbers in
    range [10, 15].
    
Python provides a random module to generate random numbers. 
To generate random numbers we have used the random 
function along with the use of the randint function.\
Syntax:

    randint(start, end)
randint accepts two parameters: a starting point and 
an ending point. 
Both should be integers and the first value 
should always be less than the second.

https://www.geeksforgeeks.org/python-generate-random-numbers-within-a-given-range-and-store-in-a-list/