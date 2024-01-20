# Write a program to remove duplicates from a list.


def remove_duplicates(some_list) -> list:
    """
    Removes duplicates from a list.

    Args:
        some_list (list): The list to remove duplicates from.

    Returns:
        some_list: A list with no duplicates.

    """
    return list(set(some_list))


# Prompt the user to enter a list
print(remove_duplicates.__doc__)
print("Enter a list: ")
LIST = input()

# Check if the input starts and ends with square brackets
if not LIST.startswith("[") or not LIST.endswith("]"):
    raise ValueError("Input must be in the format of a list")

# Remove the square brackets and split the string by commas
LIST = LIST[1:-1].split(",")

# Convert the list of strings to a list of integers
LIST = [int(num) for num in LIST]
print(LIST)

# Call the function to remove duplicates from the list
LIST = remove_duplicates(LIST)

# Display the list with no duplicates
print("The list with no duplicates is: ", LIST)
