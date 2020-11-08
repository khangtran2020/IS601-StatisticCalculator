from Statistics.Z_value import z_value
from Statistics.StandardDeviation import standarddeviation_data
from Calculator.SquareRoot import squareRoot
from Calculator.Division import division
from Calculator.Multiplication import multiplication

def MOE(data, confidence):
    return division(multiplication(z_value(confidence),standarddeviation_data(data)),squareRoot(len(data),9),9)
