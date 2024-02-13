# Write a Python program to merge two dictionaries.


def merge_dict(dict1, dict2) -> dict:
    """
    Merge two dictionaries.

    Args:
        dict1 (dict): First dictionary.
        dict2 (dict): Second dictionary.

    Returns:
        dict: Merged dictionary.
    """
    return {**dict1, **dict2}


# Test cases
print(merge_dict({1: 10, 2: 20}, {3: 30, 4: 40}))  # {1: 10, 2: 20, 3: 30, 4: 40}
print(
    merge_dict({"a": 1, "b": 2}, {"c": 3, "d": 4})
)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(merge_dict({}, {}))  # {}
