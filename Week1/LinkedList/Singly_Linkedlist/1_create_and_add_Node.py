class Node: #Define a Node Class
    def __init__(self,data):
        self.data = data
        self.next = None

#Create another class for to add nodes and link each individual nodes and define head and tail
class SinglyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,key):
        #a newNode instance is creating with the properties of Node class
        #ie a node consists of a value and a reference point to the next node
        #so can access both the properties of this class ie head,tail,.. and also the properties of the class Node
        newNode = Node(key)
        
        if self.head is None:
            #setting the first node for once and all
            self.head = newNode
        else:
            #giving the reference point of the newnode to the already end node
            self.tail.next = newNode

        #making the newnode as the tail node whose tail.next is none as default(line4)
        self.tail = newNode

    #function to display the nodes
    def display(self):
        if self.head is None:
            print("Empty List")
            return
        
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
    
#create objects and call each function 
list = SinglyLL()
list.display()

list.addNode(10)
list.addNode(20)
list.addNode(30)
list.addNode(50)
list.display()
