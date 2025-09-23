# Diffrence of two number.
def diff(num1,num2):
  n1 = num1
  n2 = num2
  diff = n1 - n2 
  print(f"Diff: {diff}") # Diff : -5
diff(5,10) 


# The given two number if first number might be lessthan Second number we a get negative number if don't want a negative notation We use this.
def diff(num1,num2):
  n1 = num1
  n2 = num2
  diff = abs(n1 - n2) # abs
  print(f"Diff: {diff}")   Diff : 5
diff(5,10)
