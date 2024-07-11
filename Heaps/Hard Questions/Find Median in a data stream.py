import heapq

# Approach: Keep appending to the stream and sort the stream.
#           Then find the median element from the stream.
class MedianFinderBruteForce:
    def __init__(self) -> None:
        self.len = 0
        self.stream = []
    
    def addNum(self, val):
        self.stream.append(val)
        self.len += 1

        self.stream.sort()
    
    def findMedian(self) -> float: 
        if self.len % 2:
            return float(self.stream[(self.len - 1)//2])
        return (self.stream[(self.len - 1)//2] + self.stream[(self.len)//2])/2
# T(n) = O(n+1 log (n+1)) for addNum, O(1) for findMedian

# Approach: Employ a min heap and max heap.
class MedianFinderOptimal:
    def __init__(self) -> None:
        self.small, self.large = [], []
    
    def addNum(self, num):
        heapq.heappush(self.small, -num)

        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    
    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        
        if len(self.large) > len(self.small):
            return float(self.large[0])

        return (-self.small[0] + self.large[0])/2
# T(n) = O(log n) for addNum, O(1) for findMedian
    
b = MedianFinderBruteForce()
b.addNum(1)
b.addNum(2)
print(b.findMedian())
b.addNum(3)
print(b.findMedian())


b = MedianFinderOptimal()
b.addNum(1)
b.addNum(2)
print(b.findMedian())
b.addNum(3)
print(b.findMedian())