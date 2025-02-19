class LiniearProbing:
    def __init__(self,size):
        self.size = size
        self.table = [None]*size
        self.count = 0  #
        self.load_factor_threshold = 0.7    #
        
    def hashFunc(self, key):
        return hash(key)%self.size
    
    def add(self, key, value):
        if self.count/self.size >= self.load_factor_threshold:  #
            self.resize()   #
        index = initial_index = self.hashFunc(key)
        while self.table[index]:
            # if self.table[index][0] == key:
            #     self.table[index] = (key,value)
            #     return
            index = (index+1) % self.size
            if index == initial_index:
                raise Exception("Hash Table is full")
        self.table[index] = (key,value)
        self.count += 1

    def __getitem__(self,key):
        index = initial_index = self.hashFunc(key)
        while self.table[index]:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index+1) % self.size
            if index == initial_index:
                break

    def delete(self,key):
        index= initial_index = self.hashFunc(key)

        while self.table[index]:
            if self.table[index][0] == key:
                self.table[index] = None
                self.count -= 1
                self.rehash(index)
                return True
            index = (index+1) % self.size
            if index == initial_index:
                break
        return False
    
    def rehash(self,start_index):
        index = start_index
        while True:
            index = (index+1) % self.size
            if self.table[index]:
                key, value = self.table[index]
                self.table[index] = None
                self.add(key,value)

    def resize(self):
        old_table = self.table
        self.size = self.size*2
        self.table = [None]*self.size
        self.count = 0

        for item in old_table:
            if item:
                self.add(item[0],item[1])

    def __str__(self):
        return str([item for item in self.table if item is not None])


hash_table = LiniearProbing(10)
hash_table.add(1,'merin')
hash_table.add(2,'maria')
hash_table.add(3,'john')
hash_table.add(3,'manukuttan')
hash_table.add(3,'ugran')
hash_table.add(3,'manukoos')
hash_table.add(1, 'disney chacha')
hash_table.add(2, 1000)

# hash_table.display()
print("After insertions:", hash_table)
hash_table.delete(23)
print("After deleting 1000:")
# hash_table.display()

print('element for 1', hash_table[1])
print('element for 2', hash_table[2])
print('element for 3', hash_table[3])
hash_table.delete(13)
print("After deleting disney chach:", hash_table)