# Using GCD Check the LCM of number:

def lcm(a,b):
    a_ = []
    b_ = []
    sum = []
    for i in range(1,a+1):
        if a % i == 0:
            a_.append(i)
    for j in range(1,b+1):
        if b % j == 0:
            b_.append(j)
    for elm in a_:
        if elm in b_:
            sum.append(elm)
    lenth = len(sum)
    gcd = sum[lenth-1]
    lcm = (a*b)//gcd
    print("LCM of",a,"and",b,"is",lcm)
lcm(12,15)