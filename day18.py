# Create a program to find the largest among three numbers.


def largest(a, b, c):
    """
    Finds the largest among three numbers.

    Args:
        a (int): First number.
        b (int): Second number.
        c (int): Third number.

    Returns:
        int: Largest number.
    """
    return max(a, b, c)


# Prompt the user to enter three numbers.
print(largest.__doc__)
print("Enter three numbers: ")
A = int(input())
B = int(input())
C = int(input())

# Call the function to find the largest among three numbers.
print(largest(A, B, C))
