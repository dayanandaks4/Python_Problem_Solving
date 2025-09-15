# Find the factorial of a number using a loop.

def fact(num):
    if num >= 0 and  num <=1:
        return 1
    else:
        return num*fact(num-1)
print(fact(num=int(input("Enter the number:"))))

