# Find the area of a circle.

# without using math module.
def area_of_circle():
    user_side_radius = float(input("Enter the radius:")) # input :5
    pi_value = 3.14159
    area_of_circle_opertion = (pi_value*(user_side_radius**2))
    print("Area of Circle is:",area_of_circle_opertion)
area_of_circle() # output: 78.53975

# using math module

import math
user_side_radius = float(input("Enter the number:"))
calc = ((math.pi)*(user_side_radius**2))
print(f"Area of circle is: {calc:.5f}")