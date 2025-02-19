class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,key):
        newNode = Node(key)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
        self.tail = newNode

    #to insert in the beginning
    def insertBeginning(self,key):
        #instance of node
        newNode = Node(key)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def insertAfter(self,key,nextTo):
        newNode = Node(key)

        if self.tail.data == nextTo:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail - newNode
            return
        
        temp = self.head
        while(temp and temp.data != nextTo):
            temp = temp.next
        if temp == None:
            print(f"there is no elem,{nextTo}")
            return
        newNode.next = temp.next
        temp.next = newNode
        newNode.prev = temp
        newNode.next.prev = newNode

    
    def insertBefore(self,key,before):
        if self.head is None:
            print("empty list")
            return
        
        newNode = Node(key)
        if key == self.head.data:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return
        
        temp = self.head

        while temp is not None and temp.data != before:
            temp = temp.next

        if temp is None:
            return
        newNode.next = temp
        temp.prev.next = newNode
        newNode.prev = temp.prev
        temp.prev = newNode

    def insertEnd(self,key):
        newNode = Node(key)
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def displayInverse(self):
        if self.head is None:
            print("empty list")
            return 
        
        print("inverse list",end="--> ")
        temp = self.tail
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev

    def display(self):
        if self.head is None:
            print("List is Empty")
            return
        temp = self.head
        while (temp is not None):
            print(temp.data, end=" ")
            temp = temp.next
        print()

list = DoublyLL()
list.addNode(1)
list.addNode(2)
list.addNode(3)
list.addNode(4)
list.addNode(5)
list.display()
print("=========------ insert beginning ------========")
list.insertBeginning(0)
list.display()
print("=========------ insert end ------========")
list.insertEnd(6)
list.display()
print("=========------ insert after ------========")
list.insertAfter(1000,4)
list.display()
print("=========------ insert before ------========")
list.insertBefore(2000,0)
list.display()
