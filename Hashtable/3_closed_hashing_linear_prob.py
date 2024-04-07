class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [None]*size
        print(self.table,"ffffffff", end=" ")
        
    def hash_fun(self, key):
        return key%self.size
    
    def add(self, key):
        index = self.hash_fun(key)
        for i in range(self.size):
            new_index = (index+i)%self.size
            if self.table[new_index] is None:
                self.table[new_index] = key
                return
        print("Hash table is full!")

    def display(self):
        print("Hash Table>>>")
        for k,v in enumerate(self.table):
            print(f"{k}:{v}")


list = HashTable(5)
list.add(12)
list.add(22)
list.add(33)
list.add(44)
list.add(444)
list.display()




print("=======-------- key and value --------=======")


# class HashTable:
#     def __init__(self,size):
#         self.size = size
#         self.table = [None]*size
#         print(self.table,"ffffffff", end=" ")
        
#     def hash_fun(self, key):
#         return key%self.size
    
#     def add(self, key,value):
#         index = self.hash_fun(key)
#         for i in range(self.size):
#             new_index = (index+i)%self.size
#             if self.table[new_index] is None:
#                 self.table[new_index] = key,value
#                 return
#         print("Hash table is full!")

#     def display(self):
#         print("Hash Table>>>")
#         for k,v in enumerate(self.table):
#             print(f"{k}:{v}")


# list = HashTable(5)
# list.add(12,4)
# list.add(22,4)
# list.add(33,4)
# list.add(44,4)
# list.add(444,4)
# list.display()
# list.add(4444,4)