class Node:
    def __init__(self, key, value):
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
            self.table[index] = Node(key, value)
        else:
            temp = self.table[index]
            while temp.next:
                if temp.key == key:
                    temp.value = value #update value if key already exists
                    return
                temp = temp.next
            temp.next = Node(key,value) #adding value to the end of chain
            #or 
            # new_node = Node(key,value)
            # new_node.next = self.table[index]  #adding value to the start of chain
            # self.table[index] = new_node


    # def get(self, key):
    #         index = self.hashFunc(key)
    #         temp = self.table[index]
    #         while temp:
    #             if temp.key == key:
    #                 return temp.value
    #             temp = temp.next 
    #         raise KeyError(key)
    def get(self, key):
        index = self.hashFunc(key)
        temp = self.table[index]
        while temp and temp.key != key:
            temp = temp.next 
        if temp is None:
            return None
        return temp.value
        
    def remove(self, key):
        index = self.hashFunc(key)
        temp = self.table[index]
        if temp and temp.key == key:
            self.table[index] = temp.next
            return
        while temp.next and temp.next.key != key:
            if temp.next.key == key:
                temp.next = temp.next.next
                return
            temp = temp.next

        
    def display(self):
        print("Hash Table:")
        for index, node in enumerate(self.table):
            print(f"{index}:", end=" ") #print index

            #if item is None, indicate an empty slot
            if node is None:
                print("None")
            #Otherwise, traverse the linked list and print key-value pairs
            else:
                current_node = node
                while current_node is not None:
                    print(f"({current_node.key}, {current_node.value})",end=" -> ")
                    current_node = current_node.next 
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

