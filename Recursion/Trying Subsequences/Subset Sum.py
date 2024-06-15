def subsetSumBruteForce(nums, target):
    def getSum(ans, nums, temp, ind, target):
        if ind == len(nums):
            if temp == target:
                ans.append(temp)
            return
        
        getSum(ans, nums, temp + nums[ind], ind + 1, target)
        getSum(ans, nums, temp, ind + 1, target)

    ans = []
    getSum(ans, nums, 0, 0, target)
    return len(ans) > 0

nums = [1, 2, 3]
target = 5

print(subsetSumBruteForce(nums, target))