# Write a program to count the occurrences of a specific character in a string.


def count_occurrences(string: str, character: str) -> int:
    """
    Counts the occurrences of a specific character in a string.

    Args:
        string (str): The input string to count occurrences from.
        character (str): The character to count occurrences of.

    Returns:
        int: The number of occurrences of the character in the string.
    """
    # Initialize a counter to keep track of the number of occurrences
    counter = 0
    # Convert the string to lowercase
    string = string.lower()
    # Loop through each character in the string
    for letter in string:
        # If the character matches the character to count, increment the counter
        if letter == character:
            counter += 1
    # Return the counter
    return counter


# Prompt the user to enter a string
print(count_occurrences.__doc__)
print("Enter a string: ")
STRING = input()

# Prompt the user to enter a character
print("Enter a character: ")
CHARACTER = input()

# Call the function to count the occurrences of the character in the string
NUMBER_OF_OCCURRENCES = count_occurrences(STRING, CHARACTER)

# Display the number of occurrences of the character in the string
print(
    "The number of occurrences of the character in the string is: ",
    NUMBER_OF_OCCURRENCES,
)
