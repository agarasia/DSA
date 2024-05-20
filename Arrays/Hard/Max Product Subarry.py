# Approach: Find all possible subarrays and check for their product
def maxProductSubarrayBruteForce(nums):
    n = len(nums)
    maxProd = -float('inf')

    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= nums[j]
            maxProd = max(maxProd, prod)
    
    return maxProd

# The pick point for this problem is that we can get the maximum 
# product from the product of two negative numbers too.

# Approach: Motivation from Kadane's algorithm
def maxProductSubarrayOptimal(nums):
    prod1 = nums[0]
    prod2 = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        temp = max(nums[i], prod1 * nums[i], prod2 * nums[i])
        prod2 = min(nums[i], prod1 * nums[i], prod2 * nums[i])
        prod1 = temp

        result = max(result, prod1)

    return result



nums = [2, 3, -2, 4]
print(maxProductSubarrayBruteForce(nums))
print(maxProductSubarrayOptimal(nums))