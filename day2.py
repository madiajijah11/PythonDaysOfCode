# Create a program to calculate the area of a circle given its radius.


def calculate_area_of_circle(radius: float) -> float:
    """
    Calculates the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    pi = 3.14
    return pi * radius * radius


# Prompt the user to enter the radius of the circle
print(calculate_area_of_circle.__doc__)
print("Enter the radius of the circle: ")
RADIUS = float(input())

# Call the function to calculate the area of the circle
AREA = calculate_area_of_circle(RADIUS)

# Display the area of the circle
print("The area of the circle is: ", AREA)
