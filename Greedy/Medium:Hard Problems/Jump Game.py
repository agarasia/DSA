def canReach(nums):
    maxReach, index = 0, 0
    while index <= maxReach:
        maxReach = max(maxReach, index + nums[index])
        if maxReach >= len(nums) - 1:
            return True
        index += 1
    
    return False
# T(n) = O(n)
# S(n) = O(1)

nums = [3, 2, 1, 0, 4]

print(canReach(nums))