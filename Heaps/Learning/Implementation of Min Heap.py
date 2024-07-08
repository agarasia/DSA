class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2
    
    def _leftChild(self, index):
        return 2*index + 1
    
    def _righChild(self, index):
        return 2*index + 2
    
    def _heapifyUpwards(self, index):
        while index and self.heap[index] < self.heap[self._parent(index)]:
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)

    def _heapifyDownwards(self, index):
        min_index = index
        left, right = self._leftChild(index), self._righChild(index)

        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left

        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
        
        if index != min_index:
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            self._heapifyDownwards(min_index)

    def insert(self, value):
        self.heap.append(value)
        self._heapifyUpwards(len(self.heap) - 1)
    
    def getMin(self):
        if not self.heap:   return None
        return self.heap[0]
    
    def extractMin(self):
        if not self.heap:   return None
        result = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapifyDownwards(0)
        return result
    
h = MinHeap()
h.insert(1)
h.insert(2)
h.insert(4)
h.insert(16)
print(h.extractMin())
print(h.extractMin())
