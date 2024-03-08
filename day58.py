# Create a function that converts a string to an integer and handles ValueError.


def convert_string_to_int(s: str) -> int:
    """Converts a string to an integer and handles ValueError.

    Args:
        s (str): A string to be converted to an integer.

    Returns:
        int: The integer value of the string.
    """
    try:
        return int(s)
    except ValueError:
        return "Invalid Input"


# Test Cases
print(convert_string_to_int("100"))  # 100
print(convert_string_to_int("1000"))  # 1000
print(convert_string_to_int("Dian Rahmadani"))  # Invalid Input
