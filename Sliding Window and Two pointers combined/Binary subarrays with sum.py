# Approach: Generate all subarrays and check if their
#           sum is equal to the target
def numSubarrayWithSumBruteForce(nums, target):
    count = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum == target:
                count += 1

    return count 
# T(n) = O(n**2)
# S(n) = O(1)

# Approach: Employ sliding window to check if the subarray
#           total is equal to the target sum
def numSubarrayWithSumOptimal(nums, target):
    count = 0
    sum = 0
    prefix_sum = {0: 1}

    for num in nums:
        sum += num
        
        if sum - target in prefix_sum:
            count += prefix_sum[sum - target]
        
        if sum in prefix_sum:
            prefix_sum[sum] += 1
        else:
            prefix_sum[sum] = 1
    
    return count
# T(n) = O(n)
# S(n) = O(n)

nums = [1,0,1,0,1]
target = 2

print(numSubarrayWithSumBruteForce(nums, target))
print(numSubarrayWithSumOptimal(nums, target))