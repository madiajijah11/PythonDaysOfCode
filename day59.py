# Create a function that checks if a number is a perfect square.


def is_perfect_square(n):
    """Check if a number is a perfect square.

    Args:
        n (int): number to check

    Returns:
        bool: True if the number is a perfect square, False otherwise
    """
    return n**0.5 == int(n**0.5)


# Test Cases
print(is_perfect_square(4))  # True
print(is_perfect_square(12))  # False
