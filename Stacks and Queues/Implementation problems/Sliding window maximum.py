# Approach: Do what we are asked to do! Create a
#           sliding window of size k and append its
#           maximum element to the ans array.
from collections import deque


def slidingWindowMaximumBruteForce(nums, k):
    def getMax(ind1, ind2):
        Max = float('-inf')
        for i in range(ind1, ind2):
            Max = max(Max, nums[i])
        return Max
    
    ans = []
    for i in range(len(nums)-k+1):
        ans.append(getMax(i, i+k))
    
    return ans
# T(n)= O(n**2)     since in the worst case, the window size is 1 and we iterate through
#                   each element twice to get the maximum.
# S(n)= O(k)        storing the answer.

# Approach: Employ a queue to keep track of which number comes in
#           and which number goes out.
def slidingWindowMaximumOptimal(nums, k):
    res = [] 
    left, right = 0, 0
    q = deque()

    while right < len(nums):
        while q and nums[right] > nums[q[-1]]:
            q.pop()
        q.append(right)

        if left > q[0]:
            q.popleft()
        
        if right + 1 >= k:
            res.append(nums[q[0]])
            left += 1
        right += 1
    
    return res
# T(n) = O(n)   where n = length of nums
# S(n) = O(n)   for storing queue and res

nums = [4, 0, -1, 3, 5, 3, 6 ,8]

print(slidingWindowMaximumBruteForce(nums, 3))