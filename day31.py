# Create a program that checks if a given string is a valid email address.


def is_valid_email(email: str) -> bool:
    """
    Create a program that checks if a given string is a valid email address.

    Args:
        email (str): A string representing an email address.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    if email.count("@") != 1:
        return False
    if email.count(".") != 1:
        return False
    if email.find("@") > email.find("."):
        return False
    return True


# Test Cases
print(is_valid_email("johndoe@mail.com"))  # True
print(is_valid_email("xxxxxxx@xxxx"))  # False
