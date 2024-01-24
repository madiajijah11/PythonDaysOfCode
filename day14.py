# Write a program to print the first n numbers of a Fibonacci sequence.


def fibonacci(n):
    """
        Print the first n numbers of a Fibonacci sequence.

    Args:
        n (int): number of Fibonacci numbers to print

    Returns:
        int: the n-th Fibonacci number

    """
    fib_sequence = [0, 1]
    while len(fib_sequence) <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n]


# Prompt user for input
print(fibonacci.__doc__)
print("Enter a number: ")
NUMBER = int(input())

# Check if the input is a number
if not isinstance(NUMBER, int):
    raise ValueError("Input must be a number")

# Call the function to print the first n numbers of a Fibonacci sequence
print(fibonacci(NUMBER))
