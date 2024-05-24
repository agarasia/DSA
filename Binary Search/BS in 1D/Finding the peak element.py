# Approach: Apply Linear search
def peakElementBruteForce(nums):
    n = len(nums)
    # Taking care of edge cases
    if n == 1:  return 0
    if nums[-1] > nums[-2]: return n-1

    for i in range(1, n-1):
        if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
            return i
# T(n) = O(n)

# Approach: Apply Binary Search
def peakElementOptimal(nums):
    n = len(nums)
    # Taking care of edge cases
    if n == 1: return 0
    if nums[-1] > nums[-2]: return n-1

    low, high = 1, n-2
    while low <= high:
        mid = low + (high-low)//2
        
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        
        # We are on the left part of the peak
        if nums[mid] > nums[mid-1]:
            low = mid + 1
        # Otherwise, we are on the right of the peak
        else:
            high = mid - 1
# T(n) = O(log n)
        

nums = [1,2,3,1]
nums2 = [1,2,1,3,5,6,4] # Either 1 or 5 can be answer since multiple peaks exist.
print(peakElementBruteForce(nums), peakElementBruteForce(nums2))
print(peakElementOptimal(nums), peakElementOptimal(nums2))