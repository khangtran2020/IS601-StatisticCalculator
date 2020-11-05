# Generate random integer and floating point decimals within a given range

Python defines a set of functions that are used to 
generate or manipulate random numbers. 
This particular type of functions are used in a 
lot of games, lotteries or any application 
requiring random number generation.

Randon Number Operations :

1. choice() :- This function is used to generate 
1 random number from a container.

2. randrange(beg, end, step) :- This function is 
also used to generate random number but within a 
range specified in its arguments. 
This function takes 3 arguments, beginning 
number (included in generation), 
last number (excluded in generation) and 
step ( to skip numbers in range while selecting).

Example: 

    import random 
    
    print ("A random number from list is : ",end="") 
    print (random.choice([1, 4, 8, 10, 3])) 
   
    print ("A random number from range is : ",end="") 
    print (random.randrange(20, 50, 3)) 
 
Output:

    A random number from list is : 4
    A random number from range is : 41

https://www.geeksforgeeks.org/random-numbers-in-python/
