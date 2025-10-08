# Simple Interest Calculation

def fun(p, t, r):
    return (p * t * r) / 100
p, t, r = 8, 6, 8
res = fun(p, t, r)
print("simple interest is:", res)

# The user can enter new values and check the simple interest.

def simple_interest():
    p = float(input("Enter the principal amount: ")) # input = 1000
    t = float(input("Enter the time in years: "))    # input = 3
    r = float(input("Enter the rate of interest: "))  # input = 5
    si = (p * t * r) / 100
    print(f"Simple interest is: {si}") # output = 150.0
simple_interest()
