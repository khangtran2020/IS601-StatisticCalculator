import numpy as np
import scipy.stats
from Statistics.StandardDeviation import standarddeviation_data
from Statistics.Zscore import z_score_transformation


def MOE(data, z):
    return z_score_transformation(z) * standarddeviation_data(data) / np.sqrt(len(data))
