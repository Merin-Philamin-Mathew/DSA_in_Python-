word = "snart"
rev = word[::-1]
string = "abhijith is a snart boy"
def check(checkword):
    if checkword == word:
        return True

for i in range(len(string)-2):
    checkword = string[i:i+(len(word))]

    if check(checkword):
        string = string[:i] +rev+ string[i+len(word):]
print(string)