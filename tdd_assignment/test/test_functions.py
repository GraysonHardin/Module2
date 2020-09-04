import unittest
from tdd_assignment.main import convert_to_months, convert_to_years


class FunctionTestCase(unittest.TestCase):
    # The first unit test validates whether the user input (1) is expected and if it is in line with the actual. The rest are the same.
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

    def test__convert_to_months__given_five_year_return_sixty_months(self):
        user_input = 5
        expected = 60

        actual = convert_to_months(user_input)

        self.assertEqual(expected, actual)
    # Slightly different than the previous tests, but same concept. The test validates whether the user's inputted months matches the expected.
    def test__convert_to_years__given_twelve_months_return_one_year(self):
        user_input = 12
        expected = 1

        actual = convert_to_years(user_input)

        self.assertEqual(expected, actual)

    def test__convert_to_years__given_twenty_four_months_return_two_year(self):
        user_input = 24
        expected = 2

        actual = convert_to_years(user_input)

        self.assertEqual(expected, actual)

    def test__convert_to_years__given_thirty_six_months_return_three_year(self):
        user_input = 36
        expected = 3

        actual = convert_to_years(user_input)

        self.assertEqual(expected, actual)

    def test__convert_to_years__given_forty_eight_return_four_year(self):
        user_input = 48
        expected = 4

        actual = convert_to_years(user_input)

        self.assertEqual(expected, actual)

    def test__convert_to_years__given_sixty_months_return_five_year(self):
        user_input = 60
        expected = 5

        actual = convert_to_years(user_input)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
