
# Sum of the first N natural numbers 
# Without using Parameter:

def sum_of_Natural_num():
    user = int(input("enter the number:"))
    n = 0
    count = 0
    while n<=user:
        count =count+n
        n+=1
    print(count)
sum_of_Natural_num()


# With using Parameter:
def sum_of_Natural_num(user):
    n = 0
    count = 0
    while n<=user:
        count =count+n
        n+=1
    print(count)
sum_of_Natural_num(5)

