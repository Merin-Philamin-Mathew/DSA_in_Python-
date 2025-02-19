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

    def deleteNode(self, key):
        if not self.head:
            return
        # Delete head
        if self.head.data == key:
            self.head = self.head.next
            return

        temp = self.head
        prev = None

        # Find node to delete
        while temp and temp.data != key:
            prev = temp 
            temp = temp.next
        if not temp:
            return
        # Update pointers
        prev.next = temp.next
        # Update tail if needed
        if temp == self.tail:
            self.tail = prev

    def deleteAfter(self,nextTo):
        if self.head is None:
            return
        temp = self.head
        while temp and temp.data != nextTo:
            temp = temp.next
        if temp and temp.next:
            if temp.next == self.tail:
                self.tail = temp
            temp.next = temp.next.next
        
    def deleteBefore(self,before):
        if self.head is None or self.head.data == before:
            return
            
        temp = self.head
        if temp.next.data == before:
            self.head = temp.next
            return
            
        while temp.next is not None and temp.next.next is not None:
            if temp.next.next.data == before:
                temp.next = temp.next.next
                return
            temp = temp.next


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