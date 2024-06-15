# Approach: generate combinations where you take or don't take the
#           the elements from array
def combinationSum(nums, target):
    def generator(ans, temp, ind, target, nums):
        if ind == len(nums):
            if  not target:
                ans.append(temp[:])
            return
            
        if nums[ind] <= target:
            temp.append(nums[ind])
            generator(ans, temp, ind, target - nums[ind], nums)
            temp.pop()
        generator(ans, temp, ind + 1, target, nums)
    ans = []
    generator(ans, [], 0, target, nums)

    return ans
# T(n) = O(2^n)     where n = length of the array

nums = [2, 3, 6, 7]
target = 7

print(combinationSum(nums, target))