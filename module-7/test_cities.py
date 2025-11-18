import unittest
from city_functions import format_city_country

class TestStringMethods(unittest.TestCase):
    def test_city_country(self):
        expected_output = 'Santiago, Chile - population 200000'
        actual_output = format_city_country('santiago', 'chile', '200000')
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()