string1 = 'jkiklolllmkuiuk'

def check_palindrome(substring):
    return substring[::-1]==substring

result = []
for index in range(1,len(string1)-1):
    i = index-1
    j = index+1
    while i>=0 and j<=len(string1):
        substring = string1[i:j+1]
        if check_palindrome(substring):
            result.append(substring)
        i -= 1
        j += 1

print(result)
