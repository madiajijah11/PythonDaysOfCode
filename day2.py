# Create a program to calculate the area of a circle given its radius.
# Prompt the user to enter the radius of the circle
print("Enter the radius of the circle: ")
RADIUS = float(input())

# Define the value of pi
PI = 3.14

# Calculate the area of the circle
AREA = PI * RADIUS * RADIUS

# Display the area of the circle with two decimal places
print("The area of the circle is: ", round(AREA, 2))
