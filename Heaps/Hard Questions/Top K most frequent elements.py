import heapq
# Approach: Find occuences and put the pairs in a maxHeap.
#           Keep popping the largest pair K times.
def kFrequentElements(nums, k):
    count = {}
    for i in nums:
        count[i] = count.get(i, 0) + 1
    
    maxHeap, ans = [], []

    for i in count:
        heapq.heappush(maxHeap, (-count[i], i))
    
    for _ in range(k):
        _, num = heapq.heappop(maxHeap)
        ans.append(num)
    
    return ans
# T(n) = O(n * log k)
# S(n) = O(n)


nums = [1, 1, 1, 2, 2, 3]
k = 2

print(kFrequentElements(nums, k))