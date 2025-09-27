# Find the square of a number without using **.

def square(num):
    squareing = num*num
    print(f"square of number is {squareing}")
square(5) # square of number is 25
square(8) # square of number is 64

# The use can enter new numbeer and check the square of the number.
def square():
    user = int(input("Enter the number:")) # input = 2
    squareing = user*user
    print(f"square of number is {squareing}") # output = 4
square()