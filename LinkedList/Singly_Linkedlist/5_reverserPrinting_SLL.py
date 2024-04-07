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
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def reverse_printing(self):
        if self.head is None:
            return
        temp = self.head
        prev = None
        while temp is not None:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = self.tail #or prev


list = SinglyLL()
lst = [1,2,3,4,5]
for i in lst:
    list.addNode(i)
list.display()

print("======------- printing reverse ------======")
list.reverse_printing()
list.display()