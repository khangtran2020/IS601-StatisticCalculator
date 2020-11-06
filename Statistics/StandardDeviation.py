from Statistics.Variance import variance_data
from Calculator.SquareRoot import squareRoot

def standarddeviation_data(data):
    var = variance_data(data)
    return squareRoot(var,9)
