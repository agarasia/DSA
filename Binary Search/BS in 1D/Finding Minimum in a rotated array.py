# Approach: Apply Linear search
def minimumBruteForce(nums):
    Min = float('inf')
    for i in nums:
        Min = min(Min, i)
    return Min

# Approach: Apply Binary Search
def minimumOptimal(nums):
    low, high = 0, len(nums) - 1
    ans = float('inf')

    while low <= high:
        mid = low + (high-low)//2
        if nums[low] <= nums[high]:
            ans = min(ans, nums[low])
            high = mid - 1
        if nums[mid] <= nums[high]:
            ans = min(ans, nums[mid])
            high = mid - 1
        else:
            ans = min(ans, nums[high])
            low = mid + 1
    
    return ans

nums = [11,13,15,17]

print(minimumBruteForce(nums))
print(minimumOptimal(nums))