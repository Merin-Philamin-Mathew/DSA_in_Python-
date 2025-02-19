string = 'merin mathew'

stack_list = []

for char in string:
    stack_list.append(char)

rev_string = ''

for i in range(len(string)):
    rev_string += stack_list.pop()

print(rev_string)



from string_reverse_node import Stack

string = "manukuttan"
node_stack = Stack()

for char in string:
    node_stack.push(char)

reverse_str = ''

while node_stack.top:
    reverse_str += node_stack.pop()

print(reverse_str)

