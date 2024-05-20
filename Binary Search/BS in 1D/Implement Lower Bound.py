# Approach: Use linear Search
def positionOfLowerBoundBruteForce(nums, target):
    n = len(nums)

    for i in range(n-1, -1, -1):
        if nums[i] <= target:   return i
    return -1

# Approach: Binary Search
def positionOfLowerBoundOptimal(nums, target):
    low, high = 0, len(nums)-1
    ans = -1

    while low <= high:
        mid = low + (high-low)//2
        if nums[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans

nums = [1,2,8,10,11,12,19]
target = 5

print(positionOfLowerBoundBruteForce(nums, target))