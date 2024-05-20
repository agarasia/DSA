# Approach: Use Linear search from front and the back
def firstAndLastOccurencesBruteForce(nums, target):
    n = len(nums)
    first, last = 0, n - 1

    while first < n and nums[first] != target:
        first += 1
    
    while last >= 0 and nums[last] != target:
        last -= 1

    if first == n: 
        first = -1
    return [first, last]

# Approach: Use Binary Search
def firstAndLastOccurencesOptimal(nums, target):
    n = len(nums)
    low, high = 0, n-1
    first, last = -1, -1

    if target not in nums:
        return [first, last]

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
    
    return [first, last]

nums = [5, 7, 7, 8, 8, 10]
target = 8

print(firstAndLastOccurencesBruteForce(nums, target))
print(firstAndLastOccurencesOptimal(nums, target))