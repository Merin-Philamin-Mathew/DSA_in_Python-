class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        #not adding the duplicates of root
        if self.key == data:
            return

        if data<self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)


    def search(self,data):
        if self.key == data:
            print("The data is found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("not found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("not found")

    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.in_order() 

    def pre_order(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()

    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key,end=" ")

    def delete(self,data,curr):
        if self.key is None:
            print("The tree is empty")
            return
        if data<self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print("Not found")
        elif data>self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print("Not found")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp=None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key,curr)
        return self


    def min_value(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("min:",current.key)

    def max_value(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("max:",current.key)

def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)
               

root = BST(20)
l = [3,5,34,22,78,6,12]
print("=========--------- INSERT -------==========")
for i in l:
    root.insert(i)

print("========----------- SEARCHING ----------========")
root.search(56)

print("========-------- DISPLAY ---------========")
root.in_order()
print()
print("========-------- DELETE ---------========")
# if count(root)>1:
#     root.delete(5,root)
# else:
#     print("not possible")
root.delete(6,root)
root.in_order()
print()
print("========-------- MIN_MAX ---------========")
root.min_value()
root.max_value()