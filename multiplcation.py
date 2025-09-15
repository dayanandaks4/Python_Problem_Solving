# Print the multiplication table of a given number.

def tables(num):
    for j in range(1, 11):
        print(f"{num} X {j} = {num*j}")
tables(6)


