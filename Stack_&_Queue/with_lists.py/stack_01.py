stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print("stack: ",stack)

n=len(stack)-1
print("last elem in stack",stack[n])

stack.pop()
print("popped->",stack)


if len(stack) == 0:
    print("stack is empty")
else:
    print("element in stack:",stack)
