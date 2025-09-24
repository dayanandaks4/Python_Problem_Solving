# Check if a number is Armstrong.
def is_armstrong_number():
    a = int(input("Enter a number: ")) # Take input from user : 153
    conv = str(a)
    lentg = len((conv))
    sum = 0
    for elm in conv:
        sum += int(elm)**lentg
    if sum == a:
        print(a,"is Armstrong")
    else:
        print(a,"is not Armstrong")
is_armstrong_number() # output: 153 is Armstrong