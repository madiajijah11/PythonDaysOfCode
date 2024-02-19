# Write a function to find the largest common divisor of two numbers using a function.


def largest_common_divisor(a, b) -> int:
    """
    Find the largest common divisor of two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The largest common divisor of the two numbers.
    """
    while b:
        a, b = b, a % b
    return a


# Test the function
print(largest_common_divisor(16, 12))
print(largest_common_divisor(9, 27))
