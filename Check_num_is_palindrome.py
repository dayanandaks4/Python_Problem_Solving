# Check if a number is a palindrome.
# It is a palindrome 
def Palindrome(num):
    convert_str = str(num)
    if convert_str == convert_str[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
Palindrome(123321)
# It is not a palindrome 
def Palindrome(num):
    convert_str = str(num)
    if convert_str == convert_str[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
Palindrome(1234)

# User can enter Run time Data and Check Whether its palindrome or not.
def Palindrome(num):
    convert_str = str(num)
    if convert_str == convert_str[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
Palindrome(num=int(input("Enter the number:")))
