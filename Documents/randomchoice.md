#Select a random item from a list

Generating random numbers has always been an useful utility in day-day programming for games or various types of gambling etc. Hence knowledge and shorthands of it in any programming language is always a plus to have.

Example:
    
    import random 
  
    test_list = [1, 4, 5, 2, 7] 
  
    print ("Original list is : " + str(test_list)) 
 
    random_num = random.choice(test_list) 
 
    print ("Random selected number is : " + str(random_num))
    
Output:

    Original list is : [1, 4, 5, 2, 7]
    Random selected number is : 1 
    
https://www.geeksforgeeks.org/python-select-random-value-from-a-list/
