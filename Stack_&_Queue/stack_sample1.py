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
        

list = Stack()
list.push(10)
list.push(20)
list.push(30)
list.push(40)
list.push(50)

#list.pop()
list.display()