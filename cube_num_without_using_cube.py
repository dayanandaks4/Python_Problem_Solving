# Find the cube of a number without using **.


def cube(num):
    squareing = num*num*num
    print(f"square of number is {squareing}")
cube(1) # cube of given number is : 1
cube(2) # cube of given number is :8

# The user can enter new number and check the cube of the number.
def cube():
    user = int(input("Enter the number:")) # input = 3
    squareing = user*user*user
    print(f"square of number is {squareing}") # output = 27
cube()