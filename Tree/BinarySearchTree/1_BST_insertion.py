class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
class BinarySearch:
    def __init__(self):
        self.root=None

    def insert(self,key):
        newNode=Node(key)
        if self.root is None:
            self.root=newNode
            return
        temp=self.root
        while temp is not None:
            if key<temp.data:
                if temp.left is None:
                    temp.left=newNode
                    return
                else:
                    temp=temp.left
            else:
                if temp.right is None:
                    temp.right=newNode
                    return
                else:
                    temp=temp.right
    def inOrder(self):
        self.inOrderHelper(self.root)
    def inOrderHelper(self,node):
        if node is not None:
            self.inOrderHelper(node.left)
            print(node.data)
            self.inOrderHelper(node.right)
list=BinarySearch()
list.insert(10)
list.insert(8)
list.insert(6)
list.insert(9)
list.insert(12)
list.insert(11)
list.insert(15)
list.inOrder()