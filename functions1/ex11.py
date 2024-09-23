def is_palindrome(input_string):
    cleaned_string = ''.join(input_string.split()).lower() # Remove spaces and lowercase
    return cleaned_string == cleaned_string[::-1]

# Example:
print(is_palindrome("madam"))           
print(is_palindrome("Hello"))           