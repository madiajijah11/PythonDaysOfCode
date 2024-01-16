# Write a program to count the occurrences of a specific character in a string.


def count_occurrences(string: str, character: str) -> int:
    """
    Counts the number of occurrences of a character in a given string.

    Args:
        string (str): The input string to count character from.
        character (str): The character to count.

    Returns:
        int: The number of occurrences of the character in the string.
    """
    # Convert the string and character to lowercase and count the number of occurrences
    return string.lower().count(character.lower())


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
