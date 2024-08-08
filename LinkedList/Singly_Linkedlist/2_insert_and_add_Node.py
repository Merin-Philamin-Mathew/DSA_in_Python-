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
        print('insert',key,' in the beginning')
        newNode = Node(key)
        newNode.next = self.head
        self.head = newNode

    def insertAfter(self,key,nextTo):
        print('insert',key,"after",nextTo)
        if self.head is None:
            return
        newNode = Node(key)
        temp = self.head
        while(temp is not None and temp.data != nextTo):
            temp = temp.next
        if temp == None:
            print(nextTo, "is not in list")
            return
        if temp == self.tail:
            self.tail.next = newNode
            self.tail = newNode
            return
        newNode.next = temp.next
        temp.next = newNode
    
    def insertBefore(self,key,before):
        print('insert',key,'before',before)
        if self.head is None:
            return
        newNode = Node(key)
        temp = self.head
        prev = None
        if temp.data == before:
            newNode.next = self.head
            self.head = newNode
            return
        while temp is not None and temp.data != before:
            prev = temp
            temp = temp.next
        if temp is None:
            print(before,'is not in the list')
            return
        newNode.next = temp
        prev.next = newNode

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
