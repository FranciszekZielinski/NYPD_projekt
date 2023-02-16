import unittest
import pandas as pd
from src import analiza

class Test(unittest.TestCase):
    def test_top_emitters(self):
        data = {'Year': [2010, 2010, 2010, 2011, 2011, 2011],
                'Country Name': ['A', 'B', 'C', 'A', 'B', 'C'],
                'co2': [100, 200, 300, 400, 500, 600],
                'population': [10, 20, 30, 40, 50, 60]}
        df = pd.DataFrame(data)

        result = analiza.top_emitters(df)

        self.assertEqual(result.shape, (6, 3))

        self.assertIn('Country Name', result.columns)
        self.assertIn('co2_per_capita', result.columns)
        self.assertIn('co2', result.columns)

    def test_top_emitters2(self):
        data = {'Year': [2010, 2010, 2010, 2011, 2011, 2011],
                'Country Name': ['A', 'B', 'C', 'A', 'B', 'C'],
                'population': [10, 20, 30, 40, 50, 60]}
        df = pd.DataFrame(data)

        result = analiza.top_emitters(df)

        self.assertEqual(result.shape, (6, 3))

        self.assertIn('Country Name', result.columns)
        self.assertIn('co2_per_capita', result.columns)
        self.assertIn('co2', result.columns)

    def test_change_in_emission(self):
        data = {'Country Name': ['A', 'B', 'C', 'A', 'B', 'C'],
                'Year': [2010, 2010, 2010, 2020, 2020, 2020],
                'co2': [100, 200, 150, 250, 50, 100],
                'population': [10, 20, 15, 25, 5, 10]}
        df = pd.DataFrame(data)

        result = analiza.change_in_emission(df)

        # Define the expected output
        expected_result = pd.DataFrame({'first': [10.0, 10, 10],
                                        'last': [10.0, 10, 10],
                                        'change': [0.0, 0.0, 0.0]},
                                        index=['A', 'B', 'C'])
        expected_result.index.name = 'Country Name'
        # Compare the actual and expected output
        self.assertTrue(result.equals(expected_result))





if __name__ == '__main__':
    unittest.main()
