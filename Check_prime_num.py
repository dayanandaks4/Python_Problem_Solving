# Check if a number is prime.
# If number is divsible by its self and 1 is called prime number.
# Its Prime number.
def prime_num(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        print("Prime number")
    else:
        print("Not a prime number")
prime_num(2)
# Its Not a prime number.

def prime_num(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        print("Prime number")
    else:
        print("Not a prime number")
prime_num(10)
# User side Enter number and Check it.

def prime_num(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        print("Prime number")
    else:
        print("Not a prime number")
prime_num(num=int(input("Enter the number:")))
