# Create a program that replaces specific words in a text with their synonyms.


def replace_synonyms(text, synonyms) -> str:
    """Replace specific words in a text with their synonyms.

    Args:
        text (str): The text to be modified.
        synonyms (list): A dictionary of words and their synonyms.

    Returns:
        str: The modified text.
    """
    for word in text.split():
        if word in synonyms:
            text = text.replace(word, synonyms[word])
    return text


# Test the function
TEXT = "I am a happy person"
SYNONYMS = {"happy": "joyful"}
print(replace_synonyms(TEXT, SYNONYMS))  # I am a joyful person.

TEXT = "She wants to go to the store"
SYNONYMS = {"wants": "desires", "store": "market"}
print(replace_synonyms(TEXT, SYNONYMS))  # She desires to go to the market.
