class Node:
    def __init__(self,data):
        self.data = data 
        self.prev = None
        self.next = None

class doublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,key):
        newNode = Node(key)

        if self.head is None:
            self.head = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
        self.tail = newNode

    def display(self):
        if  self.notEmpty():
            if self.head is None:
                print("Empty List")
                return 
            
            temp = self.head
            print("list        ",end="--> ")
            while temp and temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    def displayInverse(self):
        if self.head is None:
            print("empty list")
            return 
        
        print("inverse list",end="--> ")
        temp = self.tail
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print()
        


    def insertBeginning(self,key):
        if self.head is None:
            print("empty list")
            return
        newNode = Node(key)
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode

    def insertAfter(self,key,nextTo):
        if self.head is None:
            print("empty list")
            return
        
        newNode = Node(key)

        if self.tail.data == nextTo:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail - newNode
            return
        
        temp = self.head
        while temp and temp.data != nextTo:
            temp = temp.next

        if temp is None:
            print(f"there is no elem,{nextTo}")
            return
        newNode.next = temp.next
        temp.next = newNode
        newNode.prev = temp

        newNode.next.prev = newNode

    def notEmpty(self):
        if self.head is None:
            print("empty list")
            return False
        return True
    
    def insertBefore(self,key,before):
        if self.notEmpty():

        
            newNode = Node(key)
            if key == self.head.data:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            
            temp = self.head 

            while temp and temp.data != before:
                temp = temp.next

            if temp is None:
                return
            
            newNode.next = temp
            newNode.prev = temp.prev
            temp.prev = newNode
            newNode.prev.next = newNode

    def insertEnd(self,key):
        newNode = Node(key)
        self.teil.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

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

    def deleteAfter(self, nextTo):
        if self.notEmpty:
            
            if nextTo == self.tail.data:
                return
        
            temp = self.head

            while temp and temp.data != nextTo:
                temp = temp.next
            
            if temp is None:
                return
            
            temp.next = temp.next.next
            temp.next.prev = temp

    def deleteBefore(self, before):
        if self.notEmpty():
            
            if before == self.head:
                return 
            
            temp = self.head
            while temp and temp.data != before:
                temp = temp.next

            if temp is None:
                return 
            
            temp.prev = temp.prev.prev
            temp.prev.next = temp





dLL  = doublyLL()
dLL.display()
list = [4,56,1,3,6,4]
for i in list:
    dLL.addNode(i)
print("========================delete Node After========================")
dLL.display()
dLL.deleteAfter(3)
dLL.display()
dLL.displayInverse()
print("========================delete Node before========================")
dLL.display()
dLL.deleteBefore(3)
dLL.display()
dLL.displayInverse()
print("========================delete Node========================")
dLL.display()
dLL.deleteNode(3)
dLL.display()
dLL.displayInverse()
print("======================= insertions =====================")
dLL.insertBeginning(0)
dLL.display()
dLL.insertAfter(10,56)
dLL.insertBefore(16,10)
dLL.display()
dLL.displayInverse()
