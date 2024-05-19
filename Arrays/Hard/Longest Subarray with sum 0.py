# Approach : Find all possible subarrays and check if the sum is
#            is zero and compare the length
def longestSubarrayBruteForce(nums):
    maxlength = 0
    n = len(nums)

    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum == 0:
                maxlength = max(maxlength, j-i+1)
    return maxlength
# T(n) = O(n**2)

# Approach : Keep track of prefix sum of the elements in the array
#            and then compare its length
def longestSubarrayOptimal(nums):
    maxlength = 0
    n = len(nums)
    hashMap = {}
    sum = 0

    for i in range(n):
        sum += nums[i]
        if sum == 0:
            maxlength = i + 1
        else:
            if sum in hashMap:
                maxlength = max(maxlength, i - hashMap[sum])
            else:
                hashMap[sum] = i
    
    return maxlength
# T(n) = O(n)

nums = [15,-2,2,-8,1,7,10,23]
print(longestSubarrayBruteForce(nums))
print(longestSubarrayOptimal(nums))