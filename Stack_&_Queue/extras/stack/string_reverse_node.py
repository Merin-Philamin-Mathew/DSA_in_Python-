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

    def pop(self):
        if self.top is None:
            print("stack underflow")
            return
        data =self.top.data
        self.top = self.top.next
        return data
    

def reverse_str(string):
    stack = Stack()

    for char in string:
        stack.push(char)

    reverse_str = ""

    while stack.top:
        reverse_str += stack.pop()

    return reverse_str


print("======================reversing string=================")
print(reverse_str("merin mathew"))