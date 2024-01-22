# Write a program to reverse a given string.


def reverse_string(string) -> str:
    """
    Reverse a given string.

    Args:
        string (str): string to reverse

    Returns:
        str: reversed string
    """
    return string[::-1]


# Prompt the user to enter a string
print(reverse_string.__doc__)
print("Enter a string: ")
STRING = input()

# Check if the input is a string
if not isinstance(STRING, str):
    raise ValueError("Input must be a string")

# Call the function to reverse the string
print(reverse_string(STRING))
