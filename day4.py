# Write a program to find the sum of all elements in a list.
def calculate_sum_of_list(list_of_numbers: list) -> int:
    """
    Finds the sum of all elements in a list.

    Args:
        list_of_numbers (list): The input list to find the sum of.

    Returns:
        int: The sum of all elements in the list.
    """
    return sum(list_of_numbers)


# Prompt the user to enter a list of numbers
# Example input: [1, 2, 3, 4, 5]
LIST = input("Enter a list of numbers: ")

# Check if the input starts and ends with square brackets
if not LIST.startswith("[") or not LIST.endswith("]"):
    raise ValueError("Input must be in the format of a list")

# Remove the square brackets and split the string by commas
LIST = LIST[1:-1].split(",")

# Convert the list of strings to a list of integers
LIST = [int(num) for num in LIST]

# Call the function to find the sum of the list
SUM = calculate_sum_of_list(LIST)

print("The sum of the list is: ", SUM)
