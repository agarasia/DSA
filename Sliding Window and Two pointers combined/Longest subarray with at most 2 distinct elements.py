from collections import defaultdict

# Approach: Generate all subarrays and find the longest
#           subarray with at most 2 distinct elements.
def longestSubarrayBruteForce(nums):
    cnt = 0
    
    for i in range(len(nums)):
        st = set()
        for j in range(i, len(nums)):
            st.add(nums[i])
            if len(st) > 2:
                break

        if len(st) <= 2:
            cnt = max(cnt, cnt+1)
    
    return cnt

# Approach: Use sliding window and map to store the
#           contiguous frequency of the elements.
def longestSubarrayOptimal(arr):
    mp = defaultdict(int)
 
    i = 0  # Left pointer
    j = 0  # Right pointer
    n = len(arr)  # Length of the input array
 
    size = 0  # Size of the largest subarray with at most two distinct elements
 
    while j < n:
        # Update frequency of current element in the dictionary
        mp[arr[j]] += 1
 
        while len(mp) > 2:
            # Decrement frequency of leftmost element in the dictionary
            mp[arr[i]] -= 1
 
            # If frequency becomes zero, remove it from the dictionary
            if mp[arr[i]] == 0:
                del mp[arr[i]]
 
            i += 1  # Move left pointer to the right
 
        # Update the size of the largest subarray
        size = max(size, j - i + 1)
 
        j += 1  # Move right pointer to the right
 
    return size


nums = [2, 1, 2]
print(longestSubarrayBruteForce(nums))
print(longestSubarrayOptimal(nums))