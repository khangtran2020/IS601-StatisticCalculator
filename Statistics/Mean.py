from Calculator.Division import division

def mean_data(data):
    try:
        return division(sum(data),len(data),9)
    except ZeroDivisionError:
        print("Error: Can't divided by 0")
    except ValueError:
        print("Recheck your input")

