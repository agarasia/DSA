class Heap:
    def __init__(self) -> None:
        self.heap = []
    
    def _parent(self, index):
        return (index - 1)//2
    
    def _leftChild(self, index):
        return 2*index+1
    
    def _rightChild(self, index):
        return 2*index+2
    
    def _heapifyUpwards(self, index):
        while index and self.heap[index] > self.heap[self._parent(index)]:
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)

    def _heapifyDownwards(self, index):
        max_index = index
        left, right = self._leftChild(index), self._rightChild(index)

        if len(self.heap) > left and self.heap[left] > self.heap[max_index]:
            max_index = left
        
        if len(self.heap) > right and self.heap[right] > self.heap[max_index]:
            max_index = right
        
        if index != max_index:
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            self._heapifyDownwards(max_index)
    
    def insertInHeap(self, value):
        self.heap.append(value)
        self._heapifyUpwards(len(self.heap) - 1)
    
    def getMax(self):
        if not self.heap:
            return None
        else:
            return self.heap[0]
        
    def extractMax(self):
        if not self.heap:
            return None
        result = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapifyDownwards(0)
        return result


h = Heap()
h.insertInHeap(1)
h.insertInHeap(2)
h.insertInHeap(4)
h.insertInHeap(16)
print(h.extractMax())
print(h.extractMax())