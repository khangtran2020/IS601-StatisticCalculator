# MEDIAN
Median is the value that bigger than 50% of the data and smaller than 50% of the data. In another word, this value separate data into 2 equal parts.  

Example: 

    n_num = [1, 2, 3, 4, 5] 
    
    n = len(n_num) 
    
    n_num.sort()

    if n % 2 == 0: 

        median1 = n_num[n//2] 
        
        median2 = n_num[n//2 - 1] 
        
        median = (median1 + median2)/2
	
    else: 
    
        median = n_num[n//2] 
	
    print("Median is: " + str(median))

Output:

    Median is: 3

We define a list of numbers and calculate the length of the list. To find a median, we first sort the list in Ascending order using sort() function. Now we check if the number is even or odd by checking their remainders. If the number is even, we find 2 middle elements in a list and get their average to print it out. But if the number is odd, we find the middle element in a list and print it out.
Source: 

https://www.geeksforgeeks.org/