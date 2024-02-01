# Create a program to find the second-largest element in a list.


def second_largest_element(lists) -> int:
    """
    Find the second-largest element in a list.
    Args:
        lists (list): list to be used

    Returns:
        int: second-largest element in a list
    """
    lists.sort()
    return lists[-2]


# Testing the function
list1 = [1, 2, 3, 4, 5]
print(second_largest_element(list1))
