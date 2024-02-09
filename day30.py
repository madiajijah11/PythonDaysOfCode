# Create a function that finds the second smallest element in a list.


def second_smallest(lst) -> int:
    """
    Create a function that finds the second smallest element in a list.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The second smallest element in the list.
    """
    lst.sort()
    return lst[1]


# Test Cases
print(second_smallest([5, 4, 3, 2, 1]))  # 2
print(second_smallest([10, 5, 40, 8, 25]))  # 8
print(second_smallest([25, 143, 89, 13, 105]))  # 25
