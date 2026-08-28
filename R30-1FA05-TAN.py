import math

# Get user input
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Compute distance
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Output
print(f"\nThe distance between the two points is: {distance:.2f}")

"""
Reflection:
Using a library is much more practical than writing calculations from scratch because built-in functions like sqrt() and pow() save development time and eliminate the need to write complex algorithms manually, such as Newton's method for square roots. In this program, the math library allows us to execute accurate Euclidean distance operations in a single, readable line of code.
"""
