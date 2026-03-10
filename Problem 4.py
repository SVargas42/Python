import math

# Ask for user to enter radius
radius_input = input("Enter the radius of the circle: ")
radius = float(radius_input)

# Calculate area 
area = math.pi * (radius ** 2)

# Print final results
print(f"The area of a circle with radius {radius} is: {area:.2f}")
