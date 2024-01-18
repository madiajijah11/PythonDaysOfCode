# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.


def count_upper_lower(string) -> dict:
    """
    Counts the number of uppercase and lowercase letters in a string.

    Args:
        string (str): The string to count the letters of.

    Returns:
        dict: A dictionary containing the number of uppercase and lowercase letters.
    """
    # Use the sum function and string methods to count the number of uppercase and lowercase letters
    return {
        "uppercase": sum(1 for c in string if c.isupper()),
        "lowercase": sum(1 for c in string if c.islower()),
    }


# Prompt the user to enter a string
print(count_upper_lower.__doc__)
print("Enter a string: ")
STRING = input()

# Call the function to count the number of uppercase and lowercase letters
RESULT = count_upper_lower(STRING)

# Display the result of the count
print("The number of uppercase letters is: ", RESULT["uppercase"])
print("The number of lowercase letters is: ", RESULT["lowercase"])
