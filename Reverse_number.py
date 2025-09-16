# Reverse a number.

a = 123456   # The given number is integer .
conver_str = str(a) # The integer value not iterable so we convert int to string.
Strore_reverse_string = conver_str[::-1] # We Reverse the string value and Store it.
convert_int = int(Strore_reverse_string) # The reversed string value convert into int.
print(convert_int) # Output:654321

# Using Function 
def Reverse_num(num):
    conver_str = str(num)
    Strore_reverse_string = conver_str[::-1]
    convert_int = int(Strore_reverse_string)
    print(convert_int)
Reverse_num(987654321)
