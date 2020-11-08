from Statistics.Z_value import z_value
from Statistics.Mean import mean_data
from Statistics.StandardDeviation import standarddeviation_data
from Calculator.SquareRoot import squareRoot
from Calculator.Division import division
from Calculator.Multiplication import multiplication

def mean_confidence_interval(data, confidence=95):
    m = mean_data(data)
    # print(multiplication(z_value(confidence), standarddeviation_data(data)), squareRoot(len(data),9))
    h = division(multiplication(z_value(confidence),standarddeviation_data(data)),squareRoot(len(data),9),9)
    return m, m+h, m - h
