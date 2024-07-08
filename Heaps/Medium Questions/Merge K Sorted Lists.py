# Approach: Append to a list and return the sorted list.
def mergeKListsBruteForce(nums, k):
    ans = []
    for i in range(k):
        for j in range(k):
            ans.append(nums[i][j])
    
    ans.sort()
    return ans
# T(n) = O(k**2 log k)
# S(n) = O(k**2)

# Approach: Append to a list, heapify that list to create
#           a min heap, extract minimum elements until empty
#           to a new empty list. Return the new list.
def mergeKListsOptimal(arr, k):
    # Helper Functions
        def _heapify(nums, index):
            min_index = index
            left, right = 2*index+1, 2*index+2
            
            if left < len(nums) and nums[min_index] > nums[left]:
                min_index = left
            
            if right < len(nums) and nums[min_index] > nums[right]:
                min_index = right
            
            if min_index != index:
                nums[min_index], nums[index] = nums[index], nums[min_index]
                _heapify(nums, min_index)
        
        def _extractMin(nums):
            if len(nums) == 1:
                return nums.pop()
            result = nums[0]
            nums[0] = nums.pop()
            _heapify(nums, 0)
            return result
        
        # Driver Program
        temp, ans = [], []
        for i in range(k):
            for j in range(k):
                temp.append(arr[i][j])
        
        for i in range((k**2 - 1)//2, -1, -1):
            _heapify(temp, i)
        
        while temp:
            ans.append(_extractMin(temp))
        
        return ans
# T(n) = O(k**2 log k)
# S(n) = O(k**2)

nums = [[1, 2, 4, 4],
        [2, 2, 3, 3],
        [5, 5, 6, 6],
        [7, 8, 9, 9]]
k = 4

print(mergeKListsBruteForce(nums, k))
print(mergeKListsOptimal(nums, k))