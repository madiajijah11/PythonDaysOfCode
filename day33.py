# Write a test case for a function that checks if a number is prime.

import unittest
import math


def is_prime(n) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): Number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


# Test case
class TestIsPrime(unittest.TestCase):

    # Test with prime numbers.
    def test_prime_numbers(self):
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for number in prime_numbers:
            self.assertTrue(is_prime(number), f"{number} is prime.")

    # Test with a large prime number.
    def test_large_prime_number(self):
        number = 9999999967
        self.assertTrue(is_prime(number), f"{number} is prime.")

    # Test with a small prime number.
    def test_small_prime_number(self):
        number = 2
        self.assertTrue(is_prime(number), f"{number} is prime.")

    # Test with 0 as input.
    def test_zero_input(self):
        number = 0
        self.assertFalse(is_prime(number), f"{number} is not prime.")

    # Test with 1 as input.
    def test_one_input(self):
        number = 1
        self.assertFalse(is_prime(number), f"{number} is not prime.")

    # Test with a negative number as input.
    def test_negative_input(self):
        number = -7
        self.assertFalse(is_prime(number), f"{number} is not prime.")


# Run the test
if __name__ == "__main__":
    unittest.main()
