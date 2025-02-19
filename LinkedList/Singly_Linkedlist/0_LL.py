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
            self.tail.next =newNode
        self.tail = newNode

    def display(self):
        if self.head is None:
            print("ll is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


    def insertAfter(self, key, nextTo):
        if self.head is None:
            print("ll is empty")
            return
        newNode = Node(key)
        if nextTo == self.tail:
            self.tail.next = newNode
            self.tail = newNode
        else:
            temp = self.head
            while temp and temp.data != nextTo:
                temp = temp.next
            if temp is None:
                print("no node with data",nextTo)
            else:
                newNode.next = temp.next
                temp.next = newNode

    def insertBefore(self, key, before):
        if self.head is None:
            print("ll is empty")
            return
        newNode = Node(key)
        if before == self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            while temp.next and temp.next.data!=before:
                temp = temp.next
            if temp.next is None:
                print("there is no node with data",before)
            else:
                newNode.next = temp.next
                temp.next = newNode

    def deleteNode(self,key):
        if self.head is None:
            print("ll is empty")
            return
        if key == self.head:
            self.head = self.head.next
        else:
            temp = self.head
            while temp and temp.data != key:
                prev = temp
                temp = temp.next
            if temp is None:
                print("there is no node with data",key)
            else:
                if temp == self.tail:
                    self.tail = prev
                    self.tail.next = None
                else:
                    prev.next = temp.next


list = SinglyLL()
list.addNode(34)
list.addNode(45)
list.addNode(4)
list.addNode(78)
list.insertAfter(5,4)
list.insertBefore(10,78)
list.deleteNode(4)
list.display()