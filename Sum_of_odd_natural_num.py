# Sum of all odd numbers from 1 to N.

def sum_of_even(num):
    n = 0
    count = 0
    while n <= num:
        if n%2==0:
            count = count + n
        n+=1
    print(count)
sum_of_even(10)

