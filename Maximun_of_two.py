# Find the maximum of two numbers.
# It takes parameters.
def maximum(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2
print(maximum(num1=int(input("Enter the first number:")),num2=int(input("Enter the Second number:"))))

# It do not take parameters.
def maximum():
    num1 = int(input("Enter the First number:"))
    num2 = int(input("Enter the Second number:"))
    if num1 > num2:
        return num1
    else:
        return num2
print(maximum())
