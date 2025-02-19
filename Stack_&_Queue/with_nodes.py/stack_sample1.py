class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,key):
        newNode = Node(key)
        newNode.next = self.top
        self.top = newNode

    def display(self):
        if self.top is None:
            print("stack is empty")
            return
        temp = self.top
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def pop(self):
        print("pop--->",end="")
        if self.top is None:
            print("stack underflow")
            return
        self.top = self.top.next
        self.display()

    def reverse_str(self,string):
        stack = Stack()

        # Push each character of the string onto the stack
        for char in string:
            stack.push(char)

        # Build the reversed string by popping characters from the stack
        reversed_string = ""
        while stack.top is not None:
            reversed_string += stack.top.data
            stack.pop()

        return reversed_string
    
arr = [3,6,43,6,8,2]

stack = Stack()
for i in arr:
    stack.push(i)
stack.display()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack.reverse_str('merin'))