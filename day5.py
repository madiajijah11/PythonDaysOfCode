# Write a program to find the maximum and minimum values in a list.


def find_max_and_min(list_of_numbers: list) -> tuple:
    """
    Finds the maximum and minimum values in a list.

    Args:
        list_of_numbers (list): The input list to find the maximum and minimum values from.

    Returns:
        tuple: The maximum and minimum values in the list.
    """
    return max(list_of_numbers), min(list_of_numbers)


# Prompt the user to enter a list of numbers
print(find_max_and_min.__doc__)
# Example input: [1, 2, 3, 4, 5]
LIST = input("Enter a list of numbers: ")

# Check if the input starts and ends with square brackets
if not LIST.startswith("[") or not LIST.endswith("]"):
    raise ValueError("Input must be in the format of a list")

# Remove the square brackets and split the string by commas
LIST = LIST[1:-1].split(",")

# Convert the list of strings to a list of integers
LIST = [int(num) for num in LIST]

# Call the function to find the maximum and minimum values in the list
MAX, MIN = find_max_and_min(LIST)

print("The minimum value in the list is: ", MIN)
print("The maximum value in the list is: ", MAX)
