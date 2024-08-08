stack = []
string = 'merin mathew'
rev_string = ''

for char in string:
    stack.append(char)

for i in range(len(string)):
    rev_string += stack.pop()

print(rev_string)

