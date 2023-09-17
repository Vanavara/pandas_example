# third party
import unittest
import pandas as pd


# project
from modules.data_processing import read_csv_from_file, calculate_ema, form_candlesticks
from settings import CSV_ADDRESS


class TestDataProcessingFunctionsCsv(unittest.TestCase):
    def test_read_csv_from_file(self):
        # csv file path
        test_csv_path = CSV_ADDRESS

        # function call
        df = read_csv_from_file(test_csv_path)

        # check if the result is DataFrame
        self.assertIsInstance(df, pd.DataFrame)

        # check is DataFrame is not empty
        self.assertFalse(df.empty)


# class TestEMAFunction(unittest.TestCase):
class TestEMAFunction(unittest.TestCase):
    def test_calculate_ema(self):
        # creating test data
        data = {
            'close': [1, 2, 3, 4, 5]
        }
        df = pd.DataFrame(data)

        # call the func calculate_ema
        result = calculate_ema(df, 3)
        # check the result
        # here we are checking that that result is Serial and has a length
        # in real life we'll compare result wuth an expected EMA
        self.assertIsInstance(result, pd.Series)
        self.assertEqual(len(result), len(df))


# class TestDataProcessingFunctionsCandlesticks(unittest.TestCase):
class TestDataProcessingFynctionsCandlesticks(unittest.TestCase):
    def setUp(self):
        # creating of the test DataFrame
        data = {
            'TS': ['2023-05-04 18:21:00', '2023-05-04 18:21:30', '2023-05-04 18:22:00', '2023-05-04 18:22:30',
                   '2023-05-04 18:23:00'],
            'PRICE': [1875.979749, 1876.731348, 1876.731136, 1876.519551, 1876.153527]
        }
        self.df = pd.DataFrame(data)


    def test_from_candlestick(self):
        # call a func with 5 min interval
        result = form_candlesticks(self.df, '5T')

        # checking if the result include properly columns
        self.assertIn('open', result.columns)
        self.assertIn('high', result.columns)
        self.assertIn('low', result.columns)
        self.assertIn('close', result.columns)

        # check if the result contain one candle
        self.assertEqual(len(result), 1)

        # checking candles meaning
        self.assertEqual(result.iloc[0]['open'], 1875.979749)
        self.assertEqual(result.iloc[0]['high'], 1876.731348)
        self.assertEqual(result.iloc[0]['low'], 1875.979749)
        self.assertEqual(result.iloc[0],['close'], 1876.153527)


# if the script is run as main
if __name__ == '__main__':
    unittest.main()

