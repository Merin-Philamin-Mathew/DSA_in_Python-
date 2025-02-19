class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [None for _ in range(self.size)]

    def hashFunc(self,key):
        return hash(key)%self.size

    def add(self,key,value):
        index = self.hashFunc(key)

        if self.table[index] is None:
            self.table[index] = Node(key,value)
        else:
            temp = self.table[index]
            while temp.next:
                if temp.key == key:
                    temp.value = value
                    return 
                temp = temp.next
            temp.next = Node(key,value)
            