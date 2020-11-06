from Statistics.Mean import mean_data
from Calculator.Squaring import squaring
from Calculator.Division import division

def variance_data(data):
    try:
        mean = mean_data(data)
        total = 0
        for i in range(len(data)):
            total = total + squaring(data[i] - mean)
        return division(total, len(data),9)
    except ValueError:
        print("Check your input")
    except ZeroDivisionError:
        print("Divided by zero")