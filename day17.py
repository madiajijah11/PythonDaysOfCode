# Create a program that capitalizes the first letter of each word in a sentence.


def capitalize(sentence) -> str:
    """
    Capitalizes the first letter of each word in a sentence.

    Args:
        sentence (str): Sentence to be capitalized.

    Returns:
        str: Capitalized sentence.
    """
    return sentence.title()


# Prompt the user to enter a sentence.
print(capitalize.__doc__)
print("Enter a sentence: ")
SENTENCE = input()

# Call the function to capitalize the first letter of each word in the sentence
print(capitalize(SENTENCE))
