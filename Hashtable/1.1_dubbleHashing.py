class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
    
    def get_hash(self, key):
        return key % self.size
    
    def get_hash2(self, key):
        return 5 - (key % 5)
    
    def insert(self, key, value):
        index = self.get_hash(key)
        index2 = self.get_hash2(key)
        
        while self.table[index] is not None:
            index = (index + index2) % self.size
            print(f"key:{key} value:{value} index:{index}")

            if index == self.get_hash(key):  # Check if we have cycled back to the original index
                print("Hash Table is full")
                return
        self.table[index] = (key, value)
        print(f"key:{key} with value:{value} has been inserted in the index:{index}")

    def get(self, key):
        index = self.get_hash(key)
        index2 = self.get_hash2(key)
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + index2) % self.size
            if index == self.get_hash(key):  # Check if we have cycled back to the original index
                return None
        return None

# Example usage
hash_table = HashTable(10)
hash_table.insert(100, 1000)
hash_table.insert(200, 2000)
hash_table.insert(400, 4000)
hash_table.insert(500, 5000)

print(hash_table.get(200))  # Output should be 2000
