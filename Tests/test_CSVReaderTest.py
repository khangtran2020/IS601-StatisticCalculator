import unittest
from CSVReader.CSVReader import CSVReader,ClassFactory
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CSVReader('Tests/Data/Unit Test Addition.csv')

    def test_return_data_as_objects(self):
        result = self.csv_reader.return_data_as_class('Result')
        self.assertIsInstance(result, list)
        test_class = ClassFactory('Result', self.csv_reader.data[0])

        for res in result:
            self.assertEqual(res.__name__, test_class.__name__)
            pprint(vars(res))

if __name__ == '__main__':
    unittest.main()