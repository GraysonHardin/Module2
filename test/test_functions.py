import unittest
from main import camper_age_input
from main.camper_age_input import convert_to_months


class FunctionTestCase(unittest.TestCase):
    def test__convert_to_months__given_one_year_return_twelve_months(self):
        user_input = 1
        expected = 12

        actual = convert_to_months(user_input)

        self.assertEqual(expected, actual)


    def test__convert_to_months__given_two_year_return_twenty_four_months(self):
        user_input = 2
        expected = 24

        actual = convert_to_months(user_input)

        self.assertEqual(expected, actual)

    def test__convert_to_months__given_three_year_return_thirty_six_months(self):
        user_input = 3
        expected = 36

        actual = convert_to_months(user_input)

        self.assertEqual(expected, actual)

    def test__convert_to_months__given_four_year_return_forty_eight_months(self):
        user_input = 4
        expected = 48

        actual = convert_to_months(user_input)

        self.assertEqual(expected, actual)
    def test__convert_to_months__given_five_year_return_sixity_months(self):
        user_input = 5
        expected = 60

        actual = convert_to_months(user_input)

        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
