class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,key):
        newNode = Node(key)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode

    def display(self):
        if self.head is None:
            print("List is Empty")
            return
        temp = self.head
        while(temp is not None):
            print(temp.data)
            # print(temp.next)  #why nadeem??
            temp = temp.next

list = SinglyLL()
lst = [10,20,30,40]
for i in lst:
    list.addNode(i)
list.display()