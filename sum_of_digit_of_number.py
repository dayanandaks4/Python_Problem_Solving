# Find the sum of digits of a number.
# user can enter number and they get sum of number.

def sum_of_digit(): 
    user_side = int(input("Enter the number:"))
    conv_str = str(user_side)
    sum = 0
    for num in conv_str:
        conv_int = int(num)
        sum = sum + conv_int
    print(f"sum of number :{sum}")
sum_of_digit()
        

