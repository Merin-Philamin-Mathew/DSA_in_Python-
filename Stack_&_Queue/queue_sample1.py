class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,key):
        newNode = Node(key)
        if self.rear is None:
            self.front, self.rear = newNode, newNode
        else:
            self.rear.next = newNode
        self.rear = newNode

    def dequeue(self):
        if self.front is None:
            print("list is empty")
            return
        self.front = self.front.next
        if self.front is None:
            self.rear = None

    def display(self):
        if self.rear is None:
            print("List is Empty")
            return
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.next

list = Queue()
list.enqueue(10)
list.enqueue(20)
list.enqueue(30)
list.enqueue(40)
list.enqueue(50)
#list.dequeue()
list.display()