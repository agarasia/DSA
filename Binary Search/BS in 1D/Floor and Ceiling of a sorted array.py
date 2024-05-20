def ceilNFloor(nums, target):
    def lowerBound(nums, low, high):
        ans = -1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] <= target:
                ans = nums[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans
    
    def upperBound(nums, low, high):
        ans = -1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] >= target:
                ans = nums[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
    n = len(nums)
    low, high = 0, n-1
    ceil, floor = upperBound(nums, low, high), lowerBound(nums, low, high)
    return [floor, ceil]
    
nums = [3, 4, 4, 7, 8, 10]
target = 5

print(ceilNFloor(nums, target))