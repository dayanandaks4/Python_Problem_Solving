# Reversing the string.

def reverse_string(s):
    """
    This function takes a string as input and returns the string reversed.
    
    :param s: str - The string to be reversed
    :return: str - The reversed string
    """
    return s[::-1]
print(reverse_string("Hello, World!"))  # Output: !dlroW ,olleH
# Example usage:
print(reverse_string("Python"))          # Output: nohtyP
print(reverse_string(input("Enter a string to reverse: ")))                # Output: (the reversed string)