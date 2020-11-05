from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition


def median_data(data):
    try:
        data.sort()
        if len(data) % 2 == 0:
            median1 = data[int(len(data) // 2)]
            median2 = data[int(subtraction((data // 2), 1))]
            median_result = division(addition(median1, median2), 2, 9)
        else:
            median_result = data[int(division(len(data), 2), 9)]
        return median_result
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")