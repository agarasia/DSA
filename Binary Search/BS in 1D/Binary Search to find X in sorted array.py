def binarySearch(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high-low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid
        else:
            low = mid
    return -1

nums = [-1,0,3,5,9,12]
target = 9
print(binarySearch(nums, target))