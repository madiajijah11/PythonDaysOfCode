# Write a function to check if a number is a prime number.


def is_prime(number) -> bool:
    """
    Check if a number is a prime number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a prime number, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


# Test cases
print(is_prime(7))  # True
print(is_prime(10))  # False
