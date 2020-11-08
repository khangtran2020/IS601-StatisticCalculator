from Statistics.Mean import mean_data
from Statistics.Median import median_data
from Statistics.Mode import mode_data
from Statistics.Variance import variance_data
from Statistics.StandardDeviation import standarddeviation_data
from Statistics.Zscore import z_score_transformation
from Statistics.AdditionalModules import checkType, randomNumber
from Statistics.randomseed import seedint,seedfloat
from Statistics.randomlist import Rand
from Statistics.randomchoice import Randchoice
from Statistics.randn import randn
from Statistics.randomsample import randsample
from Statistics.randinterval import mean_confidence_interval
from Statistics.meanerror import MOE
from Statistics.cochran import Cochran
from Statistics.samplesize import samplesize

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

    def randseed(self, a, b):
        self.result = seedint(a, b)
        return self.result

    def randlist(self, a, b, c):
        self.data = Rand(a, b, c)
        return self.data

    def randomchoose(self, data):
        self.result = Randchoice(data)
        return self.result

    def randnlist(self, data, n):
        self.data = randn(data, n)
        return self.data

    def randnsample(self, data, n):
        self.data = randsample(data,n)
        return self.data

    def randinterval(self, data, confidence):
        return mean_confidence_interval(data, confidence)

    def marginerror(self, data, confidence):
        self.result = MOE(data, confidence)
        return self.result

    def cochran(self, data, conf, p = 0.5):
        self.result = Cochran(data, conf, p)
        return self.result

    def samplesze(self, conf, width, p = 0.5):
        self.result = samplesize(conf, width, p)
        return self.result