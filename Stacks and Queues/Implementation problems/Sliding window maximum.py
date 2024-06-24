# Approach: Do what we are asked to do! Create a
#           sliding window of size k and append its
#           maximum element to the ans array.
def slidingWindowMaximum(nums, k):
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

nums = [4, 0, -1, 3, 5, 3, 6 ,8]

print(slidingWindowMaximum(nums, 3))