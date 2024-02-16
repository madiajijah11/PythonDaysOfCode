# Write a program to iterate through a dictionary and print its keys and values.


def print_key_and_value_dict(dictionary):
    """
    This function prints the keys and values of a dictionary.

    Args:
        dictionary (dict): The dictionary to iterate through and print its keys and values.
    """
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")


# Test cases
print_key_and_value_dict({1: 10, 2: 20, 3: 30, 4: 40, 5: 50})
print_key_and_value_dict(
    {"a": "apple", "b": "banana", "c": "cherry", "d": "date", "e": "elderberry"}
)
