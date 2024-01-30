# Write a function that takes a list of numbers and returns a new list containing only the even numbers.


def get_even_numbers(numbers) -> list:
    """
    Takes a list of numbers and returns a new list containing only the even numbers.

    Args:
        numbers (str):  A string representing a list of numbers separated by commas.

    Returns:
        list: A list containing only the even numbers from the list of numbers.
    """
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


# Prompt the user to enter a list of numbers
print(get_even_numbers.__doc__)
print("Enter a list of numbers: ")
NUMBERS = input()

# Check if the input starts and ends with square brackets
if not NUMBERS.startswith("[") or not NUMBERS.endswith("]"):
    raise ValueError("Input must be in the format of a list")

# Remove the square brackets and split the string by commas
NUMBERS = NUMBERS[1:-1].split(",")

# Convert the list of strings to a list of integers
NUMBERS = [int(num) for num in NUMBERS]

# Call the function to get the even numbers from the list of numbers
EVEN_NUMBERS = get_even_numbers(NUMBERS)

# Display the list with only the even numbers
print("The list with only the even numbers is: ", EVEN_NUMBERS)
