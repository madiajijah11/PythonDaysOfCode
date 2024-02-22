# Write a program that removes all whitespaces from a given string.


def remove_whitespace(string) -> str:
    """
        Removes all whitespaces from a given string.

    Args:
        string (str): A string.

    Returns:
        str: A string without whitespaces.
    """
    return string.replace(" ", "")


# Test cases
print(remove_whitespace("Hello,             World!"))
