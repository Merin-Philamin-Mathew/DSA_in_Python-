class QuadraticProbingHashTable:
    def __init__(self,size):
        self.size = size
        self.table = [None]*self.size
        self.count = 0
        self.load_factor_threshold = 0.5

    def hashFunc(self,key):
        return hash(key)%self.size
    
    def __setitem__(self, key, value):
        if self.count/self.size >= self.load_factor_threshold:
            self.resize()
        index = initial_index = self.hashFunc(key)
        i = 1
        while self.table[index]:
            if self.table[index][0] == key:
                self.table[index] == (key,value)
                return
            index = (initial_index + i**2)%self.size
            i+=1
            if i>self.size:
                raise Exception("hash table is full")
        self.table[index] = (key,value)
        self.count += 1

    def __getitem__(self,key):
        index = initial_index = self.hashFunc(key)
        i = 1
        while self.table[index]:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (initial_index + i**2)%self.size
            i+=2
            if i>self.size:
                break

    def delete(self, key):
        index = initial_index = self.hashFunc(key)
        i = 1
        while self.table[index] :
            if self.table[index][0] == key:
                self.table[index] = None
                self.rehash(index)
                return True
            index = (initial_index + i**2) % self.size
            i+=1
            if i>self.size:
                break


    def rehash(self, start_index):
        for i in range(self.size):
            index = (start_index + i) % self.size

            if self.table[index]:
                key,value = self.table[index]
                self.table[index] = None
                self[key] = value

    
    def resize(self):
        new_size = self.size *2
        old_table = self.table
        self.size = new_size
        self.table = [None]*new_size
        self.count = 0

        for item in old_table:
            if item:
                self[item[0]]=item[1]

    def __str__(self):
        return str([item for item in self.table if item is not None])

        
        