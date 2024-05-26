# Approach: Test all numbers between 1 and max of 
#           max of array and the length + k
def kthMissingNumberBruteForce(nums, k):
    maxi = -float('inf')
    missing = 0

    for i in nums:
        maxi = max(maxi, i)
    
    # The maximum limit for the search space
    # could be either the max element of the array
    # or if all elements are present then the kth number.
    maxi = max(maxi, len(nums) + k)

    for i in range(1, maxi + 1):
        if i not in nums:
            missing += 1
            if missing == k:
                return i
    
    return maxi
# T(n)= O(n * max(max(nums), len(nums) + k))

# Approach : he main idea is to shift k by 1 step 
# if the current element is smaller or equal to k. 
# And whenever we get a number > k, we can conclude
#  that k is the missing number.
def kthMissingNumberBetter(nums, k):
    n = len(nums)
    for i in range(n):
        if nums[i] <= k:
            k += 1
        else:
            break
    return k
# T(n)= O(n)

def kthMissingNumberOptimal(vec, k):
    n = len(vec)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        missing = vec[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    return k + high + 1
# T(n) = O(log n)

nums = [2, 3, 4, 7, 11]
k = 5

print(kthMissingNumberBruteForce(nums, k))
print(kthMissingNumberBetter(nums, k))