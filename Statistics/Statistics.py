from Statistics.Mean import mean_data
from Statistics.Median import median_data


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
