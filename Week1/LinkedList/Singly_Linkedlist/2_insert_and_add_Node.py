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

    #to insert in the beginning
    def insertBeginning(self,key):
        #instance of node
        newNode = Node(key)
        newNode.next = self.head
        self.head = newNode

    def insertAfter(self,nextTo,key):
        newNode = Node(key)
        temp = self.head
        while(temp is not None and temp.data != nextTo):
            temp = temp.next
        if temp == None:
            return
        if temp == self.tail:
            self.tail.next = newNode
            self.tail = newNode
            return
        newNode.next = temp.next
        temp.next = newNode
    
    def insertBefore(self,before,key):
        newNode = Node(key)
        temp = self.head
        prev = None
        while temp is not None and temp.data != before:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        
        prev.next = newNode
        newNode.next = temp

    def insertEnd(self,key):
        newNode = Node(key)
        self.tail.next = newNode
        self.tail = newNode

    def display(self):
        if self.head is None:
            print("List is Empty")
            return
        temp = self.head
        while (temp is not None):
            print(temp.data, end=" ")
            temp = temp.next
        print()

list = SinglyLL()
list.addNode(10)
list.addNode(20)
list.addNode(30)
list.addNode(40)
list.display()
print("=========--- Insert Beginning ---========")
list.insertBeginning(1000)
list.display()
print("=========--- Insert End ---========")
list.insertEnd(9000)
list.display()
print("=========--- Insert After ---========")
list.insertAfter(30,9999)
list.display()
print("=========--- Insert Before ---========")
list.insertBefore(1000,1111)
list.display()