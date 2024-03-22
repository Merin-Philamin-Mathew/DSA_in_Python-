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
        temp = self.head
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def deleteNode(self,key):
        temp = self.head
        prev = None
        if temp is not None and temp.data == key:
            self.head = self.head.next
            return
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        if temp == self.tail:
            self.tail=prev
            self.tail.next = None
            return
        prev.next = temp.next

    def deleteAfter(self,key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head.next = self.head.next.next
            return
        while temp is not None and temp.data != key:
            temp = temp.next
        if temp is None or temp == self.tail:
            return
        temp.next = temp.next.next

    def deleteBefore(self,key):
        temp = self.head
        prev = None 
        if temp is None or  temp.data == key:
            return

        if temp.next is not None and temp.next.data == key:
            self.head = temp.next
            return

        while temp.next is not None and temp.next.data != key:
            prev = temp
            temp = temp.next
        if temp is None or temp.next is None:
            return
        prev.next = temp.next
    

list = SinglyLL()
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    list.addNode(i)
list.display()
print("======------- delete Node --------=======")
list.deleteNode(3)
list.display()
print("======------- delete After --------=======")
list.deleteAfter(10)
list.display()
print("======------- delete Before --------=======")
list.deleteBefore(3)
list.display()