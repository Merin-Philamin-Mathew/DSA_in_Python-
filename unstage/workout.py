class MinHeap:
    def __init__(self,array):
        self.buildHeap(array)

    def buildHeap(self,array):
        self.heap = array
        endIdx = len(self.heap)-1
        for i in range(self.parent(endIdx),-1,-1):
            self.shiftDown(i)

    def shiftDown(self,currentIdx):
        endIdx = len(self.heap)-1
        leftIdx = self.leftChild(currentIdx)
        while leftIdx <= endIdx:
            rightIdx = self.rightChild(currentIdx)
            if rightIdx <= endIdx and self.heap[rightIdx]<self.heap[leftIdx]:
                idxToShift = rightIdx
            else:
                idxToShift = leftIdx
            
            if self.heap[currentIdx] > self.heap[idxToShift]:
                self.heap[currentIdx], self.heap[idxToShift] = self.heap[idxToShift],self.heap[currentIdx]
                currentIdx = idxToShift
                leftIdx = self.leftChild(currentIdx)
            else:
                return    
            
    def shiftUp(self,currentIdx):
        parentIdx = self.parent(currentIdx)
        while currentIdx > 0 and self.heap[parentIdx]>self.heap[currentIdx]:
            self.heap[currentIdx],self.heap[parentIdx] = self.heap[parentIdx],self.heap[currentIdx]
            currentIdx = parentIdx
            parentIdx = self.parent(currentIdx)
    
    def peek(self):
        return self.heap[0]
    
    def remove(self):
        self.heap[0],self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1],self.heap[0]
        self.heap.pop()
        self.shiftDown(0)
    
    def insert(self, value):
        self.heap.append(value)
        self.shiftUp(len(self.heap)-1)
    
    def parent(self,i):
        return (i-1)//2
    
    def leftChild(self,i):
        return (2*i)+1
    
    def rightChild(self,i):
        return (2*i)+2
    
    def display(self):
        for i in range(len(self.heap)):
            print(self.heap[i],end=" ")

min_heap = MinHeap([6, 2, 8])
print("heap is:")
min_heap.display()
print()
print("=============--------INSERTION---------=============")
min_heap.insert(1)
min_heap.insert(4)
min_heap.insert(12)
min_heap.insert(0)
min_heap.display()
print()
print("=============--------REMOVAL---------=============")
min_heap.remove()
min_heap.display()