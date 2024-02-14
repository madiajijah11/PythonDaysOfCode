# Write a simple unit test for a function that adds two numbers.

import unittest


def add(a, b):
    """
        Add two numbers.

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: the sum of a and b

    """
    return a + b


class TestAdd(unittest.TestCase):
    # Adding two positive integers returns the correct sum.
    def test_add_positive_integers(self):
        assert add(2, 3) == 5

    # Adding zero to any integer returns the same integer.
    def test_add_zero_to_integer(self):
        assert add(0, 0) == 0
        assert add(0, 3) == 3
        assert add(3, 0) == 3


if __name__ == "__main__":
    unittest.main()
