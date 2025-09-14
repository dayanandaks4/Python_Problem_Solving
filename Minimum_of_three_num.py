# Find the minimum of three numbers.
# Using Parameters.
def min(num1,num2,num3):
    if num1 < num2 and num1 < num3:
        print(f"Min is {num1}")
    if num2 < num1 and num2 < num3:
        print(f"Min is {num2}")
    else:
        print(f"Min is {num3}")
min(10,6,25)

# Without Using Parameters.
def minmum():
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    num3 = int(input("Enter third number:"))
    if num1 < num2 and num1 < num3:
        print(f"Min is {num1}")
    if num2 < num1 and num2 < num3:
        print(f"Min is {num2}")
    else:
        print(f"Min is {num3}")
minmum()
