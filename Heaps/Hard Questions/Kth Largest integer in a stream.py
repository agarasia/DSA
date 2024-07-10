import heapq

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
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

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
