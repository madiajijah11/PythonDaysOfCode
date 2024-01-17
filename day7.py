# Write a program to check if a number is positive, negative, or zero.


def check_number(number: int) -> str:
    """
    Checks if a number is positive, negative, or zero.

    Args:
        number (int): The number to check.

    Returns:
        str: The result of the check.
    """
    # Check if the number is positive
    if number > 0:
        return "positive"
    # Check if the number is negative
    elif number < 0:
        return "negative"
    # Otherwise, the number is zero
    else:
        return "zero"


# Prompt the user to enter a number
print(check_number.__doc__)
print("Enter a number: ")
NUMBER = int(input())

# Call the function to check if the number is positive, negative, or zero
RESULT = check_number(NUMBER)

# Display the result of the check
print("The number is: ", RESULT)
