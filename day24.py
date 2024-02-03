# Write a program to remove vowels from a given string.


def remove_vowels(s) -> str:
    """
    Remove vowels from a given string.

    Args:
        s (str): A string.

    Returns:
        str: A string with vowels removed.
    """
    vowels = "aeiou"
    result = ""
    for char in s:
        if char.lower() not in vowels:
            result += char
    return result


# Prompt user for input
STRING = input("Enter a string: ")
print(remove_vowels(STRING))
