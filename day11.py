# Write a program to print the multiplication table of a given number.


def multiplication_table(number, multiply_by) -> None:
    """
    Prints the multiplication table of a given number.

    Args:
        number (int): The number to print the multiplication table of.
        multiply_by (int): The number to multiply the given number by.

    Returns:
        None (None): Does not return anything.
    """
    for i in range(1, multiply_by + 1):
        print(f"{number} x {i} = {number * i}")


# Prompt the user to enter a number
print(multiplication_table.__doc__)
print("Enter a number: ")
NUMBER = input()

# Check if the input is a number
if not NUMBER.isdigit():
    raise ValueError("Input must be a number")

# Prompt the user to enter a number to multiply by
print("Enter a number to multiply by: ")
MULTIPLY_BY = input()

# Check if the input is a number
if not MULTIPLY_BY.isdigit():
    raise ValueError("Input must be a number")

# Call the function to print the multiplication table
multiplication_table(int(NUMBER), int(MULTIPLY_BY))
