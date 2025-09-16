# Count the digits of a number.

def count_num(num):
    convert_str = str(num) # int values is not possible to coun convert int to str then we possible to count.
    print(len(convert_str)) 
count_num(num=int(input("Enter the number:")))
