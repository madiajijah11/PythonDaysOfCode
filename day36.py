# Write a Python program to check if two strings are anagrams.


def anagram(str1, str2):
    """
    Check if two strings are anagrams.
    Args:
        str1 (str): First string.
        str2 (str): Second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    return sorted(str1) == sorted(str2)


# Test cases
print(anagram("listen", "silent"))  # True
print(anagram("hello", "world"))  # False
