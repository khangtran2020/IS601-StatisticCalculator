from Calculator.Division import division
from Calculator.Squaring import squaring
from Calculator.Multiplication import multiplication
from Statistics.Z_value import z_value


def samplesize(conf, width, p):
    h = division(width,2,9)
    return round(multiplication(squaring(division(z_value(conf),h,9)), multiplication(p, 1-p)),0)