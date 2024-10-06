import math

def area_of_circle(radius):
    # Formula to calculate area of a circle: A = π * r^2
    return math.pi * radius ** 2

# Input: Radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate area
area = area_of_circle(radius)

# Output: Area of the circle
print(f"The area of the circle with radius {radius} is: {area:.2f}")
