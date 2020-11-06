from Statistics.Mean import mean_data
from Statistics.Median import median_data
from Statistics.Mode import mode_data
from Statistics.Variance import variance_data
from Statistics.StandardDeviation import standarddeviation_data
from Statistics.Zscore import z_score_transformation
from Statistics.AdditionalModules import checkType, randomNumber

class Statistics:
    result = 0
    data = []

    def __init__(self):
        pass

    def mean(self, data):
        self.result = mean_data(data)
        return self.result

    def median(self, data):
        self.result = median_data(data)
        return self.result

    def mode(self, data):
        self.result = mode_data(data)
        return self.result

    def var(self, data):
        self.result = variance_data(data)
        return self.result

    def std(self, data):
        self.result = standarddeviation_data(data)
        return self.result

    def z_score(self, data):
        self.data = z_score_transformation(data)
        return self.data

    def check(self, a):
        self.result = checkType(a)
        return self.result

    def rand(self, a):
        self.result = randomNumber(a)
        return self.result