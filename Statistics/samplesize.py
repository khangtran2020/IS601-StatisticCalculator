import scipy.stats as st
from math import ceil
from Statistics.meanerror import MOE
from Statistics.Zscore import z_score_transformation


def samplesize(data, z):
    p = MOE(data, z) / 2
    q = 1 - p
    sze = (z_score_transformation(z) / MOE(data, z)) ** 2
    mul = p * q
    prod = sze * mul
    return prod