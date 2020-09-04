import unittest
from cast_to_integer import cast_integer


class MyTestCase(unittest.TestCase):
    # Test unit for the integer value.
    def test__cast_integer__given_integer__returns__integer(self):
        user_input = 10
        expected = 10

        actual = cast_integer(user_input)

        self.assertEqual(expected, actual)

    def test__cast_integer__given_float_returns_integer(self):
        # Test value for the float.
        user_input = 6.5
        expected = 6

        actual = cast_integer(user_input)

        self.assertEqual(expected, actual)

    def test__cast_integer__given_string_returns_error(self):
        user_input = 'example'

        cast_integer(user_input)
        """
        ValueError: invalid literal for int() with base 10: 'example'
        This is expected. The function cannot convert a string, "example" into an integer value and thus, the test fails.
        """


if __name__ == '__main__':
    unittest.main()
