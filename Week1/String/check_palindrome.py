def is_palindrome(string):
    return string == string[::-1]

input_string = input("Enter a string:")
if is_palindrome(input_string):
    print("The string is palindrome.")
else:
    print("The string is not a palindrome.")