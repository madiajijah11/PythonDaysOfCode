# Write a program to flatten a nested list.


def flatten_list(nested_list) -> list:
    """
    Flatten a nested list.

    Args:
        nested_list (list): Nested list.

    Returns:
        list: Flattened list.
    """
    flat_list = []
    for i in nested_list:
        if type(i) == list:
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)
    return flat_list


# Test cases
print(
    flatten_list([1, 2, [3, 4, [5, 6], 7], 8, [9, 10]])
)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
