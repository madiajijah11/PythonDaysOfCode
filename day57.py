# Create a function that returns the key with the maximum value in a dictionary.


def find_key_with_max_value(d) -> int:
    return max(d, key=d.get)


# Test Cases
print(find_key_with_max_value({1: 100, 2: 200, 3: 300}))  # 3
print(find_key_with_max_value({1: 8500, 2: 800, 3: 6000}))  # 1
