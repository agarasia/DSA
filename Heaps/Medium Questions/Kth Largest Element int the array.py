# Approach: Sort the array and return the Kth element
#           from the back of the sorted array.
def kthLargestElementBruteForce(nums, k):
    nums.sort()
    return nums[len(nums) - k]
# T(n) = O(n logn)
# S(n) = O(1)

# Approach: Convert to array Max Heap, and remove k-1
#           elements and return the first element from 
#           the heapified array.
def kthLargestElementOptimal(nums, k):
    def _heapify(i):
        max_ind = i
        left, right = 2*i+1, 2*i+2

        if left < len(nums) and nums[max_ind] < nums[left]:
            max_ind = left
        
        if right < len(nums) and nums[max_ind] < nums[right]:
            max_ind = right
        
        if max_ind != i:
            nums[max_ind], nums[i] = nums[i], nums[max_ind]
            _heapify(max_ind)
    
    def _extractMax():
        res = nums[0]
        nums[0] = nums.pop()
        _heapify(0)
        return res
    
    for i in range(len(nums)//2 - 1, -1, -1):
        _heapify(i)
    
    res = -1
    for _ in range(k):
        res = _extractMax()
    
    return res
# T(n) = O(2 nlogn)
# S(n) = O(1)

nums = [3, 2, 1, 9, 6, 4]
k = 2

print(kthLargestElementOptimal(nums, k))