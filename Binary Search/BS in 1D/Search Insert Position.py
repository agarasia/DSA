def insertPositionBruteForce(nums, target):
    n = len(nums)

    for i in range(n-1, -1, -1):
        if nums[i] < target:
            return i + 1
    return -1

def insertPositionOptimal(nums, target):
    n = len(nums)
    low, high = 0, n-1
    ans = n

    while low<=high:
        mid = low + (high-low)//2
        if nums[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans

nums = [1,3,5,6]
target = 2

print(insertPositionBruteForce(nums, target))
print(insertPositionOptimal(nums, target))