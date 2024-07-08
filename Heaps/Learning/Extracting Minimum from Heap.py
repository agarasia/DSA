class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def _parent(self, index):
        return (index-1)//2
    
    def _leftChild(self, index):
        return 2*index + 1
    
    def _rightChild(self, index):
        return 2*index + 2
    
    def _heapifyUp(self, index):
        while index and self.heap[index] < self.heap[self._parent(index)]:
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)
    
    def _heapifyDown(self, index):
        min_index = index
        left, right = self._leftChild(index), self._rightChild(index)

        if left < len(self.heap) and self.heap[min_index] > self.heap[left]:
            min_index = left
        
        if right < len(self.heap) and self.heap[min_index] > self.heap[right]:
            min_index = right
        
        if min_index != index:
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            self._heapifyDown(min_index)
    
    def insert(self, value):
        self.heap.append(value)
        self._heapifyUp(len(self.heap) - 1)

    def print(self):
        print(self.heap)

    # Approach: Remove the root element from the heap
    #           and then heapify the rest of the heap.
    def extractMin(self):
        if not self.heap:
            return None
        result = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapifyDown(0)
        return result
    # T(n) = O(log n)
    # S(n) = O(1)

h = MinHeap()
h.insert(12)
h.insert(2)
h.insert(40)
h.insert(0)
h.print()
print(h.extractMin())
h.print()
