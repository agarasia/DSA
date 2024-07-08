# Approach: Recursively check for condition at left 
#           and right child nodes.
def isHeap(nums):
    def helper(index):
        left, right = 2*index+1, 2*index+2

        if index >= len(nums):
            return True

        if ((left < len(nums) and nums[left] > nums[index]) or 
            (right < len(nums) and nums[right] > nums[index])):
            return False
        
        return helper(left) and helper(right)
    
    return helper(0)

nums = [90, 15, 10, 7, 12, 2]
print(isHeap(nums), isHeap([9, 15, 10, 7, 12, 11]))