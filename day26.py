# Create a program that uses a lambda function to square each element of a list.

# Define the list
LISTS = [1, 2, 3, 4, 5]

# Use the map function with a lambda function to square each element of the list
SQUARED = list(map(lambda x: x**2, LISTS))

# Print the result
print(SQUARED)

# Output: [1, 4, 9, 16, 25]

# The `map()` function takes two arguments: a function and a list. The function is applied to each element of the list. In this example, the function is a lambda function that squares each element of the list. The result is a new list with the squared values.
