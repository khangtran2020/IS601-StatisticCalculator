from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition


def median_data(data):
    try:
        copy = [data[i] for i in range(len(data))]
        copy.sort()
        if len(data) % 2 == 0:
            left = copy[int(len(copy) // 2)]
            right = copy[int(subtraction((len(copy) // 2), 1))]
            median = division(addition(left, right), 2, 9)
        else:
            median = copy[int(division(len(copy), 2), 9)]
        return median
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")