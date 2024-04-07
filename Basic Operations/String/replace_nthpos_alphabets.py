def replace_alphabets(string, n):
    # Create a mapping of alphabets to their corresponding alphabets at the n-th position
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    mapping = {char: alphabet[(alphabet.index(char) + n) % 26] for char in alphabet}
    mapping.update({char.upper(): mapping[char].upper() for char in mapping})  # Handle uppercase alphabets
    
    # Replace each alphabet in the string with its mapped alphabet
    replaced_string = ''.join(mapping[char] if char.isalpha() else char for char in string)
    return replaced_string
# Example usage
input_string = "Hello, World!"
n = 3
output_string = replace_alphabets(input_string, n)
print("Original string:", input_string)
print("Replaced string:", output_string)


