# Z Score

Given a dataset X, z-score of an element x in X is calculate by the equation:

z = (x - mean(X))/std(X)

with std(X) is the standard deviation of dataset X. z score follows the normal distribution. 

Example:

    X = [1, 1, 2, 2, 3, 1, 4]
    
    # mean(X) = 2
    # std(X) = 1.0690449676496976
    z = []
    for i in range(len(X)):
        z.append((X[i] - mean(X))/std(X))
    
    z
    
Output
    
    array([-0.93541435, -0.93541435,  0.        ,  0.        ,  0.93541435,
           -0.93541435,  1.87082869])