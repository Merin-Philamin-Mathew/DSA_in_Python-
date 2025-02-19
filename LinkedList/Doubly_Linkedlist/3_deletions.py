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
    
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head 
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()
        
    def notEmpty(self):
        if self.head is None:
            print("empty list")
            return False
        return True
    
    def deleteNode(self,key):
        if self.notEmpty():

            if key == self.head:
                self.head = self.head.next
                self.head.prev = None
                return
            
            if key == self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
                return

            temp = self.head
            while temp and temp.data != key:
                temp = temp.next

            if temp is None:
                return
            
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp = None

    def deleteAfter(self,nextTo):
        if self.head is None:
            return
        temp = self.head
        while temp is not None and temp.data != nextTo:
            temp = temp.next
        if temp is None or temp == self.tail:
            print("Reached out of the list")
            return
        temp.next = temp.next.next
        temp.next.prev = temp
        
    def deleteBefore(self,before):
        if self.head is None:
            return
        temp = self.head
        if temp.data == before:
            print(f"Nothing before {temp.data}")
            return
        while temp is not None and temp.next.data != before:
            temp = temp.next
        if temp is None:
            print("Reached out of the List")
            return
        if temp == self.head:
            self.head = self.head.next
            return
        temp.prev = temp.next
        temp.next = temp.prev


list = DoublyLL()
lst = [1,2,3,4,5,6,7,8,9]
for i in lst:
    list.addNode(i)
list.display()

print("=======------ delete Node -------========")
list.deleteNode(5)
list.display()
print("=======------ delete After -------========")
list.deleteAfter(2)
list.display()
print("=======------ delete Before -------========")
list.deleteBefore(2)
list.display()