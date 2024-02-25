# Write a function to check if a given list is sorted.


def is_sorted(lst) -> bool:
    """Check if a given list is sorted.

    Args:
        lst (list): List to be checked.

    Returns:
        bool: True if the list is sorted, False otherwise.
    """
    return lst == sorted(lst)


# Test cases
print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 2, 3, 5, 4]))  # False
