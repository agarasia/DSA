class KthLargestBruteForce:

    def __init__(self, k: int, nums: list[int]):
        self.stream = []
        self.k = k

        for i in nums:
            self.stream.append(i)

    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream.sort(reverse=True)

        return self.stream[self.k-1]
# T(n) = O(n) for initialization, O((n+1)log(n+1)) for add
# S(n) = O(n)

class KthLargestOptimal:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        
        # Initialize the heap with the first k elements from nums
        for num in nums:
            self.add(num)
    
    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[parent] > self.heap[idx]:
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            idx = parent
            parent = (idx - 1) // 2
    
    def _sift_down(self, idx):
        child = 2 * idx + 1
        while child < len(self.heap):
            right = child + 1
            if right < len(self.heap) and self.heap[child] > self.heap[right]:
                child = right
            if self.heap[idx] <= self.heap[child]:
                break
            self.heap[idx], self.heap[child] = self.heap[child], self.heap[idx]
            idx = child
            child = 2 * idx + 1
    
    def add(self, val):
        if len(self.heap) < self.k:
            self.heap.append(val)
            self._sift_up(len(self.heap) - 1)
        elif val > self.heap[0]:
            self.heap[0] = val
            self._sift_down(0)
        
        return self.heap[0] if len(self.heap) == self.k else None


bruteForce = KthLargestBruteForce(3, [4, 5, 8, 2])
print(bruteForce.add(3))
print(bruteForce.add(5))
print(bruteForce.add(10))
print(bruteForce.add(9))
print(bruteForce.add(4))


optimal = KthLargestOptimal(3, [4, 5, 8, 2])
print(optimal.add(3))
print(optimal.add(5))
print(optimal.add(10))
print(optimal.add(9))
print(optimal.add(4))
