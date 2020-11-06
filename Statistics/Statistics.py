from Statistics.Mean import mean_data
from Statistics.Median import median_data
from Statistics.Mode import mode_data
from Statistics.Variance import variance_data

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