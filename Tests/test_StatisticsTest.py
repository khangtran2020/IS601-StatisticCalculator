import unittest
from Statistics.Statistics import Statistics
from CSVReader.CSVReader import CSVReader
import numpy as np
from scipy import stats

class MyTestCase(unittest.TestCase):

    test_data = []

    def setUp(self) -> None:
        self.statistics = Statistics()
        data = CSVReader("Tests/Data/Test_Data.csv").data
        for row in data:
            self.test_data.append(float(row['value1']))

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_statistic_mean(self):
        self.assertEqual(self.statistics.mean(self.test_data), np.mean(self.test_data))
        self.assertEqual(self.statistics.result, np.mean(self.test_data))

    def test_statistic_mode(self):
        self.assertEqual(self.statistics.mode(self.test_data), stats.mode(self.test_data).mode[0])
        self.assertEqual(self.statistics.result, stats.mode(self.test_data).mode[0])

    def test_statistic_median(self):
        self.assertEqual(self.statistics.median(self.test_data), np.median(self.test_data))
        self.assertEqual(self.statistics.result, np.median(self.test_data))

    def test_statistic_variance(self):
        self.assertEqual(self.statistics.var(self.test_data), round(np.var(self.test_data),9))
        self.assertEqual(self.statistics.result, round(np.var(self.test_data),9))

    def test_statistic_std(self):
        self.assertEqual(self.statistics.std(self.test_data), round(np.std(self.test_data),9))
        self.assertEqual(self.statistics.result, round(np.std(self.test_data),9))

    def test_statistic_z_score(self):
        z_test = self.statistics.z_score(self.test_data)
        z_result = stats.zscore(self.test_data)
        for i in range(len(z_test)):
            self.assertEqual(z_test[i], round(z_result[i],6))

    def test_checkType(self):
        self.assertEqual(self.statistics.check(self.test_data), type(self.test_data))

    def test_randomeseed(self):
        self.assertEqual(self.statistics.randseed(self.test_data))

    def test_randlist(self):
        self.assertEqual(self.statistics.randlist(self.test_data))

    def test_randchoose(self):
        self.assertEqual((self.statistics.randomchoose()))

    def test_randnlist(self):
        self.assertEqual(self.statistics.randnlist(self.test_data))

    def test_randnsample(self):
        self.assertEqual(self.statistics.randnsample(self.test_data))

    def test_randinterval(self):
        self.assertEqual(self.statistics.randinterval(self.test_data))

    def test_moe(self):
        self.assertEqual(self.statistics.marginerror(self.test_data))

    def test_cochran(self):
        self.assertEqual(self.statistics.randcochran(self.test_data))

    def test_samplesze(self):
        self.assertEqual(self.statistics.samplesze(self.test_data))



if __name__ == '__main__':
    unittest.main()
