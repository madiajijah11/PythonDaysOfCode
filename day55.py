# Create a function that takes a string and returns the reverse of each word.


def reverse_each_word(txt) -> str:
    """Reverse Each Word

    Args:
        txt (str): string to reverse

    Returns:
        str: reverse of each word
    """
    return " ".join([i[::-1] for i in txt.split()])


print(reverse_each_word("The quick brown fox"))  # "ehT kciuq nworb xof"
print(reverse_each_word("Hello World"))  # "olleH dlroW"
