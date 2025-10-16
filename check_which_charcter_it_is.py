# 50.	Check if a character is uppercase, lowercase, digit, or special symbol.
def check_character_type(char):
    if char.isupper():
        return "Uppercase"
    elif char.islower():
        return "Lowercase"
    elif char.isdigit():
        return "Digit"
    else:
        return "Special Symbol"
print(check_character_type('A'))  # Output: Uppercase
print(check_character_type('a'))  # Output: Lowercase
print(check_character_type('1'))  # Output: Digit
print(check_character_type('@'))  # Output: Special Symbol
