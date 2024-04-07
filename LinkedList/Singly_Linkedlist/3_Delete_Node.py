class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
class SinglyLl:
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
            print("List is empty")
            return
        temp = self.head 
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def deleteNode(self,key):
        if self.head is None:
            return
        temp = self.head
        prev = None
        if temp.data == key:
            self.head = temp.next
            return
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        if temp == self.tail:
            self.tail = prev
            self.tail.next = None
            return
        prev.next = temp.next

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
        
    def deleteBefore(self,before):
        if self.head is None:
            return
        temp = self.head
        prev = None
        if temp.data == before:
            print(f"Nothing before {temp.data}")
            return
        while temp is not None and temp.next.data != before:
            prev = temp
            temp = temp.next
        if temp is None:
            print("Reached out of the List")
            return
        if temp == self.head:
            self.head = self.head.next
            return
        prev.next = temp.next


list = SinglyLl()
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