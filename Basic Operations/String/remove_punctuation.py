import string 

def remove_punctuation(str1):
    return ''.join(char for char in str1 if char not in string.punctuation)

input_string = "Hello, World! This is a test string."
cleaned_string = remove_punctuation(input_string)
print("String without punctuation:", cleaned_string)