# Write a function to count the number of vowels in a given string.
def count_vowels(string):
    """
    Counts the number of vowels in a given string.

    Args:
        string (str): The input string to count vowels from.

    Returns:
        int: The number of vowels in the string.
    """
    # Initialize a counter to keep track of the number of vowels
    counter = 0
    # Define a list of vowels
    vowels = ["a", "e", "i", "o", "u"]
    # Loop through each character in the string
    for letter in string:
        # If the character is a vowel, increment the counter
        if letter in vowels:
            counter += 1
    # Return the counter
    return counter


# Prompt the user to enter a string
print(count_vowels.__doc__)
print("Enter a string: ")
STRING = input()

# Call the function to count the number of vowels in the string
NUMBER_OF_VOWELS = count_vowels(STRING)

# Display the number of vowels in the string
print("The number of vowels in the string is: ", NUMBER_OF_VOWELS)
