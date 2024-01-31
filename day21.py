# Create a program to remove a specific element from a set.


def remove_element(sets, element) -> set:
    """
    Remove a specific element from a set.
    Args:
        sets (set): set to be used
        element (any): element to be removed

    Returns:
        set: set without the element
    """
    sets.remove(element)
    return sets


# Testing the function
set1 = {1, 2, 3, 4, 5}
print(remove_element(set1, 3))
