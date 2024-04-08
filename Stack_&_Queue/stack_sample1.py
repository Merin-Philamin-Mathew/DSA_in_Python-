class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None

    def push(self,key):
        newNode = Node(key)
        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode

    def pop(self):
        if self.top is None:
            print("stack underflow")
            return 
        self.top = self.top.next

    def display(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def reverse_str(self, string):
        # Create an empty stack
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

list = Stack()
list.push(10)
list.push(20)
list.push(30)
list.push(40)
list.push(50)

#list.pop()
list.display()
str = "aalrib atat"
reversed = list.reverse_str(str)
print(reversed)