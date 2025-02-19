class Hashtable:
    def __init__(self,size):
        self.size = size
        self.arr = self.size*[None]

    def getHash(self,key):
        h = key
        if isinstance(key,str):
            h=0
            for char in key:
                h+=ord(char)
        return h%self.size
    
    def add(self,key,value):
        index = self.getHash(key)
        self.arr[index] = value
    
    def __setitem__(self,key,value):
        index = self.getHash(key)
        self.arr[index]=value

    def __getitem__(self,key):
        index = self.getHash(key)
        return self.arr[index]
        # print("key:",key," value:",self.arr[index])

    def get(self,key):
        index = self.getHash(key)
        print("key:",key," value:",self.arr[index])

    def display(self):
        for index,value in enumerate(self.arr):
            print(index,": ",value)
    

lists = Hashtable(6)
lists['age'] = 24
lists['merin'] = 'mathew'
lists['merin']
lists.add('maria','manu')
lists.get('age')
lists.display()
print("=================== EXAMPLE2 ==================")
hashtable = Hashtable(6)
hashtable[1] = 'maria'
hashtable[3] = 'john'
hashtable[2] = 'merin'
hashtable['maria'] = 1
hashtable['merin'] = 2
hashtable['john'] = 3

print(hashtable[2])
print(hashtable['merin'])

hashtable.display()
