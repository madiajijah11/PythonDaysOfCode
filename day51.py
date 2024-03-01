# Create a program that counts the occurrences of each word in a text file


def count_words(file) -> dict:
    """Count the occurrences of each word in a text file

    Args:
        file (str): The file to be read

    Returns:
        dict: A dictionary containing the occurrences of each word
    """
    with open(file, "r", encoding="utf-8") as f:
        words = f.read().split()
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count


# Test cases
print(count_words("text.txt"))
