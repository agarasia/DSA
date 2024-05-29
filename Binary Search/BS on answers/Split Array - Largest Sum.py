# Approach: Refer to Allocating m books problem.
def smallestLargestSumBruteForce(nums, subarrays):
    def splitArrays(sum):
        n = len(nums)
        arrays = 1
        totalSum = 0

        for i in range(n):
            if totalSum + nums[i] <= sum:
                totalSum += nums[i]
            else:
                arrays += 1
                totalSum = nums[i]

        return arrays

    n = len(nums)
    if n == 1:
        return nums[0]
    if subarrays > n:   return -1

    maxElement, sumElements = max(nums), sum(nums)
    for acc in range(maxElement, sumElements+1):
        if splitArrays(acc) == subarrays:
            return acc
        
    return maxElement

def smallestLargestSumOptimal(nums, subarrays):
    def splitArrays(sum):
        n = len(nums)
        arrays = 1
        totalSum = 0

        for i in range(n):
            if totalSum + nums[i] <= sum:
                totalSum += nums[i]
            else:
                arrays += 1
                totalSum = nums[i]
                
        return arrays

    n = len(nums)
    if n == 1:
        return nums[0]
    if subarrays > n:   return -1

    low, high = max(nums), sum(nums)
    while low <= high:
        mid = low + (high-low)//2
        splits = splitArrays(mid)

        if splits > subarrays:
            low = mid + 1
        else:
            high = mid - 1
            
    return low

nums = [1, 2, 3, 4, 5]
subarrays = 3

print(smallestLargestSumBruteForce(nums, subarrays))