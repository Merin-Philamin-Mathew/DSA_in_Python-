def capitalize_first_letter(string):
    return ' '.join(word.capitalize() for word in string.split())
input_string = "he,llo world th,is is a test string"
capitalized_string = capitalize_first_letter(input_string)
print("Capitalized string:", capitalized_string)


sentence = "This, is a sam,ple sentence."
words = sentence.split(",")  # Split the sentence into words based on whitespace
print(words)
