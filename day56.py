# Create a function to extract all URLs from a given text using regular expressions.

import re


def extract_URLs(text) -> list[str]:
    """Extract all URLs from a given text using regular expressions.

    Args:
        text (str): A string containing URLs.

    Returns:
        list[str]: A list of URLs.
    """
    return re.findall(r"(https?://\S+)", text)


# Test cases
print(extract_URLs("https://www.google.com"))  # ['https://www.google.com']
print(
    extract_URLs("https://www.google.com https://www.facebook.com")
)  # ['https://www.google.com', 'https://www.facebook.com']
print(
    extract_URLs(
        "lorem ipsum https://www.google.com lorem ipsum https://www.facebook.com lorem ipsum https://www.instagram.com"
    )
)  # ['https://www.google.com', 'https://www.facebook.com', 'https://www.instagram.com']
