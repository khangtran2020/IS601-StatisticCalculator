from Statistics.Mean import mean_data

class Statistics:
    result = 0
    data = []

    def __init__(self):
        pass

    def mean(self, data):
        self.result = mean_data(data)
        return self.result
