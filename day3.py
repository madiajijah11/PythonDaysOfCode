# Write a function to count the number of vowels in a given string.
def count_vowels(string: str) -> int:
    """
    Counts the number of vowels in a given string.

    Args:
        string (str): The input string to count vowels from.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase and count the number of vowels using the sum and in-built count function
    return sum(string.lower().count(vowel) for vowel in "aeiou")


# Prompt the user to enter a string
print(count_vowels.__doc__)
print("Enter a string: ")
STRING = input()

# Call the function to count the number of vowels in the string
NUMBER_OF_VOWELS = count_vowels(STRING)

# Display the number of vowels in the string
print("The number of vowels in the string is: ", NUMBER_OF_VOWELS)
