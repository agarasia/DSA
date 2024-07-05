# Approach: Generate all subarrays and check if the subarray is Nice.
def numberOfSubarraysBruteForce(nums, k):
    ans = 0
    for i in range(len(nums)):
        count = 0
        for j in range(i, len(nums)):
            if nums[j] % 2:
                count += 1
            if count == k:
                ans += 1
                break
    
    return ans
# T(n) = O(n**2)
# S(n) = O(1)

# Approach: Use sliding window to keep track of number of odd numbers.
def numberOfSubarraysOptimal(nums, k):
    def atMost(k):
        left = 0
        ans = 0
        count = 0

        for right in range(len(nums)):
            if nums[right] % 2:
                count += 1
            
            while count > k:
                if nums[left] % 2:
                    count -= 1
                
                left += 1
            
            ans += (right - left + 1)
        
        return ans
    
    return atMost(k) - atMost(k-1)
# T(n) = O(n)
# S(n) = O(1)

nums = [1, 1, 2, 1, 1]
k = 3

print(numberOfSubarraysBruteForce(nums, k))
print(numberOfSubarraysOptimal(nums, k))