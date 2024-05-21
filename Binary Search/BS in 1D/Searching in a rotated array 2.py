# Approach: Use Linear Search
def searchBruteForce(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:   return True
    return False

def searchOptimal(nums, target):
    low, high = 0, len(nums)-1

    while low <= high:
        mid = low + (high-low)//2

        if nums[mid] == target:
            return True
        
        if nums[mid] == nums[low] == nums[high]:
            high -= 1
            low += 1
            continue
        
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

    return False

nums = [1,1,0,1,1,2]
target = 0

print(searchBruteForce(nums, target))
print(searchOptimal(nums, target))