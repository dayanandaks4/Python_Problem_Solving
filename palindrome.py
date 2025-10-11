# Check if a string is a palindrome.
def is_palindrome(s):
    """
    This function checks if the given string is a palindrome.

    :param s: str - The string to be checked
    :return: bool - True if the string is a palindrome, False otherwise
    """
    # Normalize the string by removing spaces and converting to lowercase
    normalized_str = ''.join(s.split()).lower()
    # Check if the normalized string is equal to its reverse
    return normalized_str == normalized_str[::-1]
# Example usage:
print(is_palindrome("A man a plan a canal Panama"))  # Output: True
print(is_palindrome("Hello"))                         # Output: False   
print(is_palindrome(input("Enter a string to check for palindrome: ")))  # Output: True/False based on input
