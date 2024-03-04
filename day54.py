# Create a function to find all words in a sentence that start with a vowel.


def find_vowel_words(sentence):
    """
    Find all words in a sentence that start with a vowel.

    Args:
        sentence: The sentence to search.

    Returns:
        A list of words that start with a vowel.
    """
    return [word for word in sentence.split() if word[0].lower() in "aeiou"]


# Test cases
print(find_vowel_words("The quick brown fox jumps over the lazy dog"))
print(find_vowel_words("The cat in the hat"))
