def getLength(a):
    if (len(a.split('.')) > 1):
        return len(a.split('.')[1])
    else:
        return 0