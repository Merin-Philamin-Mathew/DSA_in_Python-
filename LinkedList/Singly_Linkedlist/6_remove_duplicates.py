class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def addNode(self,key):
        newNode=Node(key)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode

    # def remove_duplicates(self):
    #     if self.head is None:
    #         return
    #     temp = self.head
    #     while temp.next is not None:
    #         if temp.data == temp.next.data:
    #             temp.next = temp.next.next
    #         else:
    #             temp = temp.next
     
    def removeDuplicates(self):
        if self.head is None:
            return
        values = set()
        temp = self.head
        prev = None
        while temp is not None:
            if temp.data in values:
                prev.next = temp.next
            else:
                values.add(temp.data)
                prev = temp
            temp = temp.next

    def display(self):
        if self.head is None:
            print("List is empty")
        temp = self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
        print()

list = SinglyLL()
lst = [10,20,10,30,50,60,50,30,40]
for i in lst:
    list.addNode(i)
list.display()
print("======------- removing duplicates ------======")
list.removeDuplicates()
list.display()