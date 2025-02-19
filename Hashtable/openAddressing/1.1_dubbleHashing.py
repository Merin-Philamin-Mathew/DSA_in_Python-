class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [None]*size

    def hashFunc(self,key):
        h = key
        if isinstance(key, str):
            h = 0 
            for char in key:
                h += ord(char)
        return h%self.size
    
    def hashFunc2(self,key):
        return 5 - key%5
    
    def __setitem__(self, key, value):
        index = self.hashFunc(key)
        index2 = self.hashFunc2(key)

        while self.table[index]:
            # # editing existing
            # if self.table[index][0] == key:
            #     self.table[index] = (key,value)
            #     return
            
            index = (index+index2) % self.size
            print(f"key:{key} value:{value} index:{index}")

            if index == self.hashFunc(key):
                print("hash Table is full, failed to insert key:",key,'value:',value)
                return

        self.table[index] = (key,value)
        print(f"key:{key} with value:{value} has been inserted in the index:{index}")

    def __getitem__(self, key):
        index = self.hashFunc(key)
        index2 = self.hashFunc2(key)

        while self.table[index]:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index+index2)%self.size
            if index == self.hashFunc(key):
                return None
            
    def display(self):
        for index,value in enumerate(self.table):
            print(f"{index}: {value}")

    def __str__(self):
        return str([item for item in self.table if item])
            
hash_table = HashTable(10)
hash_table[1] = 'merin'
hash_table[2] = 'maria'
hash_table[3] = 'john'
hash_table[3] = 'manukuttan'
hash_table[3] = 'ugran'
hash_table[3] = 'manukoos'
hash_table[3] = 'disney chacha'
hash_table[3] = 1000

print(hash_table[3])

hash_table.display()
print(hash_table)