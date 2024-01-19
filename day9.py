# Write a program to check if a number is even or odd.


def is_even_or_odd(number: int) -> str:
    """
    Checks if a number is even or odd.

    Args:
        number (int): The number to check.

    Returns:
        str: A string containing the result of the check.
    """
    # Check if the number is even
    if number % 2 == 0:
        # Return a string saying that the number is even
        return "The number is even."
    # Otherwise
    else:
        # Return a string saying that the number is odd
        return "The number is odd."


# Prompt the user to enter a number
print(is_even_or_odd.__doc__)
print("Enter a number: ")
NUMBER = int(input())

# Call the function to check if the number is even or odd
RESULT = is_even_or_odd(NUMBER)

# Display the result of the check
print(RESULT)
