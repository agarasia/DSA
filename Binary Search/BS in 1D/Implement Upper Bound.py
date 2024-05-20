def positionOfUpperBound(nums, target):
    low, high = 0, len(nums)-1
    ans = -1
    
    while low <= high:
        mid = low + (high-low)//2
        if nums[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans

nums = [1, 2, 2, 3]
target = 2
print(positionOfUpperBound(nums, target))