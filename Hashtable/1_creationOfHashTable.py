class Hashtable:
    def __init__(self,size):
        self.size = size
        self.table = [None]*self.size #[None for i in range(self.size)]

        print(self.table)

    def hash_fun(self,value):
        # Simple modulo hashing based on table size
        # generating the key or index for adding the value
        return value%self.size
    
    def add(self, value):
        index = self.hash_fun(value)
        self.table[index] = value

    def get(self, value):
        return value%self.size
    
    def display_pairs(self):
        print("Key-Value Pairs:")
        for index, item in enumerate(self.table):
            print(f"{index}: {item}")

list = Hashtable(10)
list.add(12)
list.add(23)
list.add(45)
list.add(10)
list.add(10)
print(list.get(45))
list.display_pairs()
