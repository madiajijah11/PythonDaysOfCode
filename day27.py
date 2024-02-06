# Create a program that sorts a list of strings alphabetically.
#
# Define the list of strings
LISTS = ["banana", "apple", "orange", "cherry", "grape"]

# Use the `sorted()` function to sort the list of strings
SORTED = sorted(LISTS)

# Print the result
print(SORTED)

# Output: ['apple', 'banana', 'cherry', 'grape', 'orange']

# The `sorted()` function takes a list as an argument and returns a new list with the elements sorted in ascending order. In this example, the list of strings is sorted alphabetically.

# The `sorted()` function can also take an optional argument `key` that specifies a function to be applied to each element of the list before sorting. For example, to sort the list of strings by length, you can use the `len` function as the `key` argument:
#
# LISTS = ['banana', 'apple', 'orange', 'cherry', 'grape']
# SORTED
