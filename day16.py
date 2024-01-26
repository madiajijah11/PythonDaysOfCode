# Write a function that counts the frequency of each word in a sentence.


def word_frequency(sentence) -> dict:
    """
    Write a function that counts the frequency of each word in a sentence.

    Args:
        sentence (str): The sentence to count the frequency of each word.

    Returns:
        dict: A dictionary containing the frequency of each word.
    """
    words = sentence.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


# Prompt the user to enter a sentence.
print(word_frequency.__doc__)
print("Enter a sentence: ")
SENTENCE = input()

# Call the function to count the frequency of each word in the sentence
print(word_frequency(SENTENCE))
