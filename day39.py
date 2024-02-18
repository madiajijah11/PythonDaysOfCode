# Write a program to find the most common words in a text file.


def find_common_words(file_name):
    """
    Find the most common words in a text file.

    Args:
        file_name (str): The name of the file to read.
    """
    with open(
        file_name,
        "r",
        encoding="utf-8",
    ) as file:
        words = file.read().split()
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        print(word_count)
        max_word = max(word_count, key=word_count.get)
        print(
            f"The most common word is '{max_word}' with {word_count[max_word]} occurences."
        )


# Test the function
find_common_words("text.txt")
