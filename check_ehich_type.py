# Check if a character is uppercase, lowercase, digit, or special symbol.
user = input("Enter the chracter:")
if user == user.upper():
    print(f"The given character is upper")
elif user == user.lower():
    print(f"The given character is lower")
elif user == user.isdigit():
    print(f"The given character is digit")
else:
    print("givem chracter is special character")