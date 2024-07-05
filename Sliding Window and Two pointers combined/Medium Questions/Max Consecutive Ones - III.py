# Approach: Keep a shifting sliding window to keep track of 
#           maximum permissible zeros.
def maxConsecutiveOnes(nums, k):
    l, r, zeros = 0, 0, 0
    ans = float('-inf')

    while r < len(nums):
        if nums[r] == 0:
            zeros += 1
        
        if zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        
        if zeros <= k:
            ans = max(ans, r - l + 1)

        r += 1
    
    return ans
# T(n) = O(n)
# S(n) = O(1)

nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

print(maxConsecutiveOnes(nums, k))