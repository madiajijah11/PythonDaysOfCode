# Write a program that reads an integer from the user and handles invalid inputs.


def read_integer() -> int:
    """
        Reads an integer from the user and handles invalid inputs.

    Returns:
        int: An integer.
    """
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue


# Test cases
print(read_integer())
