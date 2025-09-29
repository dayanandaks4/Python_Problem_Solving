# Convert Celsius to Fahrenheit.
def convert_celsius_to_fahrenheit(c):
    f = ((9/5)*c)+32
    print(f"{c} of Fahrenheit is {int(f)} degree F")
convert_celsius_to_fahrenheit(25)

# User can enter Run time Data and Convert Celsius to Fahrenheit.
def convert_celsius_to_fahrenheit():
    c = int(input("Enter the temperature in Celsius: ")) # 25
    f = ((9/5)*c)+32
    print(f"{c} of Fahrenheit is {int(f)} degree F")
convert_celsius_to_fahrenheit()


