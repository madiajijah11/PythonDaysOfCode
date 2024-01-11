# Create a program that swaps the value of two variables
# Get input from the user
print("Enter two value, whatever it's words, numbers, anything")
print("Enter the first value: ")
FIRST_VALUE = str(input())
print("Enter the second value: ")
SECOND_VALUE = str(input())

# Display the values before swapping
print("Before swapping: ")
print("a = ", FIRST_VALUE)
print("b = ", SECOND_VALUE)

# Swap the values
FIRST_VALUE, SECOND_VALUE = SECOND_VALUE, FIRST_VALUE

# Display the values after swapping
print("After swapping: ")
print("a = ", FIRST_VALUE)
print("b = ", SECOND_VALUE)
