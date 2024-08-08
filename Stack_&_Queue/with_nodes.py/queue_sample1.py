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
        if self.front is None:
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode

    def dequeue(self):
        if self.front is None:
            print('nothing to dequeue')
        else:
            print("dequeue-->",end="")
            self.front = self.front.next
            self.display()

    def display(self):
        if self.front is None:
            print("queue is empty")
        temp = self.front
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

list = Queue()
list.enqueue(3)
list.enqueue(4)
list.enqueue(5)
list.enqueue(6)
list.display()
list.dequeue()
list.dequeue()
list.dequeue()
list.dequeue()
