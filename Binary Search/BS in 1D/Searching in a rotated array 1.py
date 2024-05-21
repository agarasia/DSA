# Approach: Apply linear search
def searchBruteForce(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:   return i
    
    return -1

# Approach: Modify binary search algorithm
def searchOptimal(nums, target):
    low, high = 0, len(nums)-1

    while low <= high:
        mid = low + (high-low)//2

        if nums[mid] == target:
            return mid
        
        if nums[low] <= nums[mid]:
            if nums[low] <= target and target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:
            if nums[mid] <= target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


nums = [4,5,6,7,0,1,2]
target = 0

print(searchBruteForce(nums, target))
print(searchOptimal(nums, target))