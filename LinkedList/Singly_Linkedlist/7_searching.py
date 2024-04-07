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

    def searchNode(self,key):
        pos = 1
        temp = self.head
        #Loop until node with key is found or end of list is reached
        while temp is not None and temp.data != key:
            pos += 1
            temp = temp.next
        
        #Check if key was found
        if temp is not None:
            return pos
        else:
            return -1
        

list = SinglyLL()
lst = [10,20,30,40,50,60]
for i in lst:
    list.addNode(i)
list.display()
print("========------- searching node -------========")
position = list.searchNode(60)

if position == -1:
    print("Key not found")
else:
    print(f"Key found at position {position}")