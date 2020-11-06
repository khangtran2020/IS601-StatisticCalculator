from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean_data
from Statistics.StandardDeviation import standarddeviation_data

def z_score_transformation(data):
    copy = [division(subtraction(data[i],mean_data(data)),standarddeviation_data(data),9) for i in range(len(data))]
    return copy