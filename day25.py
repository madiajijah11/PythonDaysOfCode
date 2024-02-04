# Create a program to concatenate two lists.


def list_concatenate(list1, list2) -> list:
    """
    Concatenates two lists.

    Args:
        list1 (list): first list
        list2 (list): second list

    Returns:
        list: list1 + list2
    """
    return list1 + list2


# Test cases
print(list_concatenate([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
print(list_concatenate([1, 2, 3], []))  # [1, 2, 3]
