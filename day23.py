# Write a program that checks if a key exists in a dictionary.


def check_key(dictionary, key):
    """
    Check if a key exists in a dictionary.

    Args:
        dictionary (dict): The dictionary to check.
        key (str): The key to check for.

    Returns:
        bool: True if the key exists, False otherwise.
    """
    if key in dictionary:
        return True
    else:
        return False


# Test function
print(check_key({"a": 1, "b": 2, "c": 3}, "a"))  # True
print(check_key({"a": 1, "b": 2, "c": 3}, "d"))  # False
