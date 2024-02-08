# Create a function that generates a random number between a given range.
import random


def random_number(start, end) -> int:
    """
    This function generates a random number between a given range.

    Args:
        start (int): Start of the range.
        end (int): End of the range.

    Returns:
        int: Random number between the given range.
    """
    return random.randint(start, end)


# Prompting the user to enter the range.
print(random_number.__doc__)
START = int(input("Enter the start of the range: "))
END = int(input("Enter the end of the range: "))

# Printing the random number between the given range.
print(f"Random number between {START} and {END} is: {random_number(START, END)}")
