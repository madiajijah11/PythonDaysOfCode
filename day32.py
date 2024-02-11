# Create a function that calculates the average of a list of numbers.


def average(lst) -> int:
    """
    Calculate the average of a list of numbers.

    Args:
        lst (list): a list of numbers

    Returns:
        int: the average of the list
    """
    return sum(lst) / len(lst)


# Test Cases
print(average([1, 2, 3, 4, 5]))  # 3
print(average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 5.5
