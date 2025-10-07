# Function to calculate the area of a triangle given its base and height.

def area_of_triangle(base,height):
    return 0.5*base*height
print(f"area of the triangle is :{area_of_triangle(2,10)}")

# user can enter base and height to find the area of triangle.

print(f"area of the triangle is :{area_of_triangle(int(input('Enter base: ')), int(input('Enter height: ')))}")