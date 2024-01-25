# Create a program that checks if a year is a leap year.


def is_leap_year(year) -> bool:
    """
    Checks if a year is a leap year.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Prompt the user to enter a year.
print(is_leap_year.__doc__)
print("Enter a year: ")
YEAR = int(input())

# Check if the input is a number
if not isinstance(YEAR, int):
    raise ValueError("Input must be a number")

# Call the function to check if the year is a leap year
print(is_leap_year(YEAR))
