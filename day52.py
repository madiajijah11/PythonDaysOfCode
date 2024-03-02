# Create a program that checks if a string is a palindrome.


def is_palindrome(words):
    """Check if a string is a palindrome.

    Args:
        words (str): A string to check if it is a palindrome.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    words = words.lower()
    words = words.replace(" ", "")
    return words == words[::-1]


# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
