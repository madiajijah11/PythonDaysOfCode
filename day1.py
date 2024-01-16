# Create a program that swaps the value of two variables


def swaps_the_value_of_two_variables(variable1: str, variable2: str) -> tuple:
    """
    Swaps the value of two variables.

    Args:
        variable1 (str): The first variable.
        variable2 (str): The second variable.

    Returns:
        tuple: The swapped values of the two variables.
    """
    return variable2, variable1


# Get input from the user
print(swaps_the_value_of_two_variables.__doc__)
print("Enter the first value: ")
FIRST_VALUE = str(input())
print("Enter the second value: ")
SECOND_VALUE = str(input())

# Display the values before swapping
print("Before swapping: ")
print("the first value = ", FIRST_VALUE)
print("the second value = ", SECOND_VALUE)

# Call the function to swap the values of the two variables
FIRST_VALUE, SECOND_VALUE = swaps_the_value_of_two_variables(FIRST_VALUE, SECOND_VALUE)

# Display the values after swapping
print("After swapping: ")
print("the first value = ", FIRST_VALUE)
print("the second value = ", SECOND_VALUE)
