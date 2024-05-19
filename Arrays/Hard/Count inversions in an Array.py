# Approach: Manually check for all possible inversions
def inversionsBruteForce(nums):
    n = len(nums)
    count = 0

    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                count += 1
            else:
                continue
    
    return count

nums = [5,4,3,2,1]
print(inversionsBruteForce(nums))