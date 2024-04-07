class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [None for i in range(self.size)]


    def hash_fun(self,key):
        return hash(key)%self.size
    
    def add(self,key,value):
        index = self.hash_fun(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            temp = self.table[index]
            while temp.next is not None:
                # if temp.key == key:
                #     temp.value = value
                #     return
                temp = temp.next
            temp.next = Node(key,value)
            #or 
            # new_node = Node(key,value)
            # new_node.next = self.table[index]
            # self.table[index] = new_node


    # def get(self, key):
    #         index = self.hash_fun(key)
    #         temp = self.table[index]
    #         while temp:
    #             if temp.key == key:
    #                 return temp.value
    #             temp = temp.next 
    #         raise KeyError(key)
    def get(self, key):
        index = self.hash_fun(key)
        temp = self.table[index]
        while temp is not None and temp.key != key:
            temp = temp.next 
        if temp is None:
            return None
        else:
            return temp.value
        
    def remove(self, key):
        index = self.hash_fun(key)
        temp = self.table[index]
        if temp and temp.key == key:
            self.table[index] = temp.next
            return
        while temp is not None and temp.next.key != key:
            temp = temp.next
        if temp is None:
            return None
        temp.next = temp.next.next

        
    def display(self):
        print("Hash Table:")
        for index, item in enumerate(self.table):
            print(f"{index}:", end=" ") #print index

            #if item is None, indicate an empty slot
            if item is None:
                print("None")
            #Otherwise, traverse the linked list and print key-value pairs
            else:
                current = item
                while current is not None:
                    print(f"({current.key}, {current.value})",end=" -> ")
                    current = current.next 
                print("end") #Mark the end of the chain

    def __contains__(self, key):
        if self.get(key) != None:
            return True
        return False

ht= HashTable(10)
ht.add(10,"hello")
ht.add(23,"Merin")
ht.add(34,"how")
ht.add("45","are")
ht.add(56,"you")
ht.add(65,"?")
ht.add("merin",54)
print("==========---------- display --------===========")
ht.display()
print("==========---------- remove --------===========")
ht.remove("merin")
ht.display()
print("==========----------  get   --------===========")
print(ht.get(56))
print(ht.get("56"))
print("==========---------- replace --------===========")
#uncomment lines 23-25
ht.add(34,"HOW!!")
ht.display()
print("==========---------- checking --------===========")
print(56 in ht)
print("45f" in ht)

