from Statistics.meanerror import MOE
from Statistics.Z_value import z_value
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Squaring import squaring

def Cochran(data, conf, p = 0.5):
    return division(multiplication(squaring(z_value(conf)),multiplication(p,1-p)), squaring(1 - conf/100), 0) + 1
