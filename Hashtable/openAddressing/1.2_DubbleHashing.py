class DoubleHashingTable:
    def __init__(self,size):
        self.size = size
        self.table = [None]*size
        self.count = 0
        self.load_factor_threshold = 0.6

    def hashFunc(self, key):
        return hash(key)%self.size
    
    def hashFunc2(self, key):
        return 1 + (hash(key)%(self.size)-2)
    
    def __setitem__(self, key, value):
        if self.count / self.size >= self.load_factor_threshold:
            self.resize()

        index = initital_index = self.hashFunc(key)
        index2 = self.hashFunc2(key)


        while self.table[index]:
            # editing existing // comment it and see
            if self.table[index][0] == key:
                self.table[index] = (key,value)
                return
            
            index = (index+index2) % self.size
            if index == initital_index:
                print("HashTable is Full")
                raise Exception("HashTable is Full")
            
        self.table[index] = (key,value)
        self.count += 1

    def __getitem__(self,key):
        index = initial_index = self.hashFunc(key)
        index2 = self.hashFunc2(key)

        while self.table[index]:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index+index2) % self.size
            if index == initial_index:
                return None
    def delete(self,key):
        index = initial_index = self.hashFunc(key)
        index2 = self.hashFunc2(key)

        while self.table[index]:
            if self.table[index][0] == key:
                self.table[index] = None
                self.count -= 1
                self.rehash(index)
                return True
            index = (index+index2) % self.size
            if index == initial_index:
                return None
            
    def rehash(self, start_index):
        for i in range(self.size):
            index = (start_index+i) % self.size
            if self.table[index] is None:
                continue
            key, value = self.table[index]
            self.table[index] = None
            self[key] = value
    
            
    def resize(self):
        old_table = self.table
        self.size = self.find_next_prime(self.size*2)
        self.table = [None]*self.size
        self.count = 0  # Reset count temporarily

        for item in old_table:
            if item:
                self[item[0]] = item[1] # This will increment self.count appropriately
                # self.insert(item[0],item[1])

    def find_next_prime(self, n):
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        while not is_prime(n):
            n += 1
        return n
    

    def __str__(self):
        return str([[index,item] for index,item in enumerate(self.table) if item])
            
    def display(self):
        for index,value in enumerate(self.table):
            print(f"{index}: {value}")
            


hash_table = DoubleHashingTable(10)
hash_table[1] = 'merin'
hash_table[2] = 'maria'
hash_table[3] = 'john'
hash_table[3] = 'manukuttan'
hash_table[3] = 'ugran'
hash_table[3] = 'manukoos'
hash_table[13] = 'disney chacha'
hash_table[23] = 1000

# hash_table.display()
print(hash_table)
hash_table.delete(23)
print("After deleting 1000:")
# hash_table.display()
print(hash_table)

print("After insertions:", hash_table)
print('element for 1', hash_table[1])
print('element for 2', hash_table[2])
print('element for 3', hash_table[3])
hash_table.delete(13)
print("After deleting disney chach:", hash_table)