def count_vowels_consonants(string):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    count_vowels = 0
    count_consonants = 0
    for alph in string:
        if alph.lower() in vowels:
            count_vowels += 1
        elif alph.lower() in consonants:
            count_consonants += 1
    # num_vowels = sum(1 for char in string if char.lower() in vowels)
    # num_consonants = sum(1 for char in string if char.lower() in consonants)
    return count_vowels, count_consonants

input_string = "Me Ma"
vowels, consonants = count_vowels_consonants(input_string)
print(f"count of vowels, {vowels}")
print(f"count of consonants, {consonants}")

