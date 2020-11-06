# Standard Deviation 

Standard Deviation measures how far a data set is spread out. It is mathematically defined as square root of variance.
The difference between Variance and Standard Deviation is the units of the data.

Given a dataset X, variance can be calculated by the equation:  

STD = Sqrt(Sum((x - mean(X))^2)/n)

With n is the number of data points in the dataset X.

Example:

    X = [1, 1, 2, 2, 3, 1, 4]
    
    # mean(X) = 2
    total = 0
    for i in range(len(X)):
        total = total + (X[i] - mean(X))**2
    var(X) = total/len(X)
    std(X) = sqrt(var(x))
    
Output:
    
    1.0690449676496976