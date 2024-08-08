class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self,index):
        return (index - 1)//2
    
    def _left_child(self,index):
        return 2*index+1
    
    def _right_child(self,index):
        return 2*index +2
    
    def _heapify_up(self,index):
        parent = self._parent(index)
        # iterate index from end to root>> len(self.heap)-1 to 0
        # if parent's value is greater>> swap
        if index>0 and self.heap[index]<self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = self._left_child(index)
        right = self._right_child(index)
        smallest = index

        # iterate index from root to end>> 0 to len(self.heap)
        # and find the smallest child to swap it with root(parent) of every subtree
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def insert(self, element):
        # insert element to the end ie len(self.heap)-1 then correct the position by heapify up
        self.heap.append(element)
        self._heapify_up(len(self.heap)-1)

    def extract_min(self):
        # if heap is empty
        if not self.heap:
            return None
        # extract_min == extract root
        if len(self.heap)==1:
            return self.heap.pop()
        root = self.heap[0]
        #giving the root max value(lst node) and then heapify it from the root to end
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        # extract_min == extract root
        return root
    
    def peak_min(self):
        return self.heap[0] if self.heap else None

    def __str__(self):
        return str(self.heap)



min_heap = MinHeap()
array = [3,10,5,1,4,6,8,7,2]
for i in array:
    min_heap.insert(i)

print("Min-heap:", min_heap)
print("Extract Min:",min_heap.extract_min())
print("Min-heap after extraction:", min_heap)
print("Peak Min:", min_heap.peak_min())