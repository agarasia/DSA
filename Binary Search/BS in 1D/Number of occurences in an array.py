def occurencesBruteForce(nums, target):
    first, last = -1, -1

    for i in range(len(nums)):
        if nums[i] == target:
            first = i
            break
    
    for j in range(len(nums)-1, -1, -1):
        if nums[j] == target:
            last = j
            break

    if first == -1 and last == -1:  
        return 0
    return last-first+1

def occurencesOptimal(nums, target):
    n = len(nums)
    low, high = 0, n-1
    first, last = -1, -1

    while low <= high:
        mid = low + (high-low)//2
        if nums[mid] >= target:
            first = mid
            high = mid - 1
        else:
            low = mid + 1

    low, high = 0, n-1
    while low <= high:
        mid = low + (high-low)//2
        if nums[mid] <= target:
            last = mid
            low = mid + 1
        else:
            high = mid - 1
    
    if first == -1: return 0
    return last-first+1

nums = [1,1,2,2,2,2,3]
target = 1

print(occurencesBruteForce(nums, target))
print(occurencesOptimal(nums, target))