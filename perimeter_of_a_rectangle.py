# Find the perimeter of a rectangle.

def perimeter_of_rectangle(length, breadth):
    return 2 * (length + breadth)
print(f"Perimeter of rectangle is: {perimeter_of_rectangle(2, 2)}")
print(f"Perimeter of rectangle is: {perimeter_of_rectangle(int(input('Enter length: ')), int(input('Enter breadth: ')))}")