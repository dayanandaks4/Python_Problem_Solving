# Find the cube of a number without using **.

def cube(num):
    cubing = num*num*num
    print(f"cube of number is {cubing}")
cube(1) # cube of given number is : 1
cube(2) # cube of given number is :8

# The user can enter new number and check the cube of the number.

def cube():
    user = int(input("Enter the number:")) # input = 3
    cubing = user*user*user
    print(f"cube of number is {cubing}") # output = 27
cube()
