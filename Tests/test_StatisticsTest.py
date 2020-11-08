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
        self.assertEqual(self.statistics.randseed(1,10), self.statistics.randseed(1,10))

    def test_randlist(self):
        # print(len(self.test_data))
        data1 = self.statistics.randlist(1, 50, 10)
        data2 = self.statistics.randlist(1, 50, 10)
        for i in range(10):
            self.assertEqual(data1[i],data2[i])
        # print(len(self.test_data))

    def test_randchoose(self):
        # print(len(self.test_data))
        self.assertEqual(self.statistics.randomchoose(self.test_data), self.statistics.randomchoose(self.test_data))

    def test_randnlist(self):
        data1 = self.statistics.randnlist(self.test_data, 10)
        data2 = self.statistics.randnlist(self.test_data, 10)
        for i in range(10):
            self.assertEqual(data1[i], data2[i])

    def test_randnsample(self):
        data1 = self.statistics.randnsample(self.test_data, 10)
        data2 = self.statistics.randnsample(self.test_data, 10)
        for i in range(10):
            self.assertEqual(data1[i], data2[i])


    def test_randinterval(self):
        self.test_data = []
        data = CSVReader("Tests/Data/Test_Data.csv").data
        for row in data:
            self.test_data.append(float(row['value1']))

        m1, left1, right1 = self.statistics.randinterval(self.test_data, 95)
        self.assertEqual(m1, 99.3155)
        self.assertEqual(left1, 100.183310845)
        self.assertEqual(right1, 98.447689155)

    def test_moe(self):
        self.test_data = []
        data = CSVReader("Tests/Data/Test_Data.csv").data
        for row in data:
            self.test_data.append(float(row['value1']))

        moe = self.statistics.marginerror(self.test_data, 95)
        self.assertEqual(moe, 0.867810845)

    def test_cochran(self):
        self.assertEqual(self.statistics.cochran(self.test_data, 95, 0.5), 385)

    def test_samplesze(self):
        self.assertEqual(self.statistics.samplesze(95,0.06,0.41), 1033)



if __name__ == '__main__':
    unittest.main()
