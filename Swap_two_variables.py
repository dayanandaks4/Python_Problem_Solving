#Swap two variable With and Without using Variables.

#Without using third variable
def swap(num1,num2):
    num_1 = num1
    num_2 = num2
    
    num_1,num_2 = num2,num1
    print(f"num_1:{num_1}\nnum_2:{num_2}")
swap(5,10)


# With using third varaible
def swap(num1,num2):
    num_1 = num1
    num_2 = num2
    
    temp = num_1
    num_1 = num_2
    num_2 = temp
  
    print(f"num_1:{num_1}\nnum_2:{num_2}")
swap(5,10)

