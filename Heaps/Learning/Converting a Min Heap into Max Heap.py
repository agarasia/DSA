# Approach: Use heapifyDown approach.
def convertToMaxHeap(nums):
    def heapifyDown(i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < len(nums) and nums[left] > nums[largest]:
            largest = left
        
        if right < len(nums) and nums[right] > nums[largest]:
            largest = right
        
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapifyDown(largest)
    
    # Perform heapify starting from the last non-leaf node to the root node
    for i in range(len(nums) // 2 - 1, -1, -1):
        heapifyDown(i)
    
    return nums
# T(n) = O(log n)
# S(n) = O(1)

nums = [1, 2, 3, 4]

print(convertToMaxHeap(nums))