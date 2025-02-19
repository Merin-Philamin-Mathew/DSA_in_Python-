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

    def notEmpty(self):
        if self.head is None:
            print("Empty list")
            return False
        return True

    def display(self):
        if self.notEmpty():
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
        print()

    def mergeLL(self, list):
        if self.notEmpty():
            self.tail.next = list.head
            list.head.prev = self.tail
            self.tail = list.tail
        


arr1 = [2,3,4,5]
arr2 = [6,7,8,9]

list1 = DoublyLL()
list2 = DoublyLL()

for i in arr1:
    list1.addNode(i)
list1.display()

for i in arr2:
    list2.addNode(i)
list2.display()

list1.mergeLL(list2)
list1.display()
list2.display()