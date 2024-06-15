# Approach: Generate all possible subsets and
#           check which one has not been added
#           to the answer already.
def possibleSubsetsBruteForce(nums):
    def generate(nums, ans, temp, ind):
        if len(nums) == ind:
            if temp not in ans:
                ans.append(temp[:])
            return
        
        temp.append(nums[ind])
        generate(nums, ans, temp, ind + 1)
        temp.pop()
        generate(nums, ans, temp, ind + 1)

    if not nums:
        return []
    ans = []
    generate(nums, ans, [], 0)
    return ans
# T(n) = O(2^n)     where n = length of the array

# Approach: Optimization for not choosing duplicate elements,
#           thus not forming duplicate subsets.
def possibleSubsets(nums):
    def generate(ind, temp, ans, nums):
        ans.append(temp[:])
        for i in range(ind, len(nums)):
            if i != ind and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
            generate(i + 1, temp, ans, nums)
            temp.pop()

    if not nums:
        return []
    
    nums.sort()
    
    ans = []
    generate(0, [], ans, nums)
    return ans
# T(n) = O(2^n)     where n = length of array

nums = [1, 2, 2]

print(possibleSubsetsBruteForce(nums))
print(possibleSubsets(nums))