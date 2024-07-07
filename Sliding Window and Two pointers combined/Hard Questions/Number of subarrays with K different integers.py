# Approach: Generate all subarrays and check if they
#           have at most K distinct integers.
def numberOfSubarraysBruteForce(nums, k):
    def atMost(k):
        ans = 0
        for i in range(len(nums)):
            count = {}
            for j in range(i, len(nums)):
                count[nums[j]] = count.get(nums[j], 0) + 1
                if len(count) <= k:
                    ans += 1
        return ans
    
    return atMost(k) - atMost(k-1)

# Approach: Employ sliding window to find the number of
#           subarrays with at most K different integers
def numberOfSubarraysOptimal(nums, k):
    def atMost(k):
        left = 0
        ans = 0
        hashMap = {}
        for right in range(len(nums)):
            hashMap[nums[right]] = hashMap.get(nums[right], 0) + 1
            
            while len(hashMap) > k:
                hashMap[nums[left]] -= 1
                
                if hashMap[nums[left]] == 0:
                    del hashMap[nums[left]]

                left += 1
            
            if len(hashMap) <= k:
                ans += (right - left + 1)
        
        return ans
    
    return atMost(k) - atMost(k-1)
# T(n) = O(n)
# S(n) = O(n)

nums = [1, 2, 1, 2, 3]
k = 2

print(numberOfSubarraysBruteForce(nums, k))
print(numberOfSubarraysOptimal(nums, k))