class Node: #Define a Node Class
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

#Create another class for to add nodes and link each individual nodes and define head and tail
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

    #function to display the nodes
    def display(self):
        if self.head is None:
            print("Empty List")
            return
        
        temp = self.head
        while temp is not None:
            #print(temp.prev,end=" ")
            print(temp.data,end=" ")
            #print(temp.next,end=" ")
            #print()
            temp = temp.next
        print()
#create objects and call each function 
list = DoublyLL()
list.display()

list.addNode(10)
list.addNode(20)
list.addNode(30)
list.addNode(50)
list.display()
