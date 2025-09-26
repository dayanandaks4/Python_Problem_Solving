# Find the product of digits of a number.

def product_of_digit():
    a = input("Enter the number:") # 123
    sum = 1
    for num in a:
        sum = sum*int(num)
    print(sum)   # output:6
product_of_digit()


