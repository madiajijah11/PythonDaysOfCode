# Write a function to calculate the factorial of a number.


def calculate_factorial(n) -> int:
    """
    Calculates the factorial of a number.

    Args:
        n (int): Number.

    Returns:
        int: Factorial of a number.
    """
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)


# Prompt the user to enter a number.
print(calculate_factorial.__doc__)
print("Enter a number: ")
N = int(input())

# Call the function to calculate the factorial of a number.
print(calculate_factorial(N))
