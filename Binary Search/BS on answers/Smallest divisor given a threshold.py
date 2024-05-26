from math import ceil

# Approach: Check all possible divisor
def smallestDivisorBruteForce(nums, threshold):
    # Helper function: is the divisor within 
    #                  the threshold
    def isWithinThreshold(divisor):
        combinedSum = 0

        for i in nums:
            combinedSum += ceil(i / divisor)
        
        return combinedSum <= threshold

    # Driver Code
    mini, maxi = float('inf'), -float('inf')

    for i in nums:
        mini = min(mini, i)
        maxi = max(maxi, i)
    
    # Check for all possible divisors if the
    # combined sum within the threshold.
    for i in range(mini, maxi + 1):
        if isWithinThreshold(i):
            return i
    
    return -1
# T(n)= O(n * maxi)

# Approach: Optimize checking process using 
#           binary search
def smallestDivisor(nums, threshold):
    # Helper function: is the divisor within 
    #                  the threshold
    def isWithinThreshold(divisor):
        combinedSum = 0

        for i in nums:
            combinedSum += ceil(i / divisor)
        
        return combinedSum <= threshold
    
    # Driver Code
    low, high = 1, -float('inf')
    ans = 0

    for i in nums:
        high = max(high, i)
    
    while low <= high:
        mid = low + (high-low)//2
        if isWithinThreshold(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans
# T(n)= O(n * log(maxi))

nums = [44,22,33,11,1]
threshold = 5

print(smallestDivisorBruteForce(nums, threshold))
print(smallestDivisor(nums, threshold))