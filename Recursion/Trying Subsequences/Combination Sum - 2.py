# Approach: Generate all possible answer tuples and
#           if not in ans, append the tuple
def combinationSumBruteForce(nums, target):
    def generate(ans, temp, ind, target, nums):
        if ind == len(nums):
            if not target and sorted(temp[:]) not in ans:
                ans.append(sorted(temp[:]))
            return

        if nums[ind] <= target:
            temp.append(nums[ind])
            generate(ans, temp, ind + 1, target - nums[ind], nums)
            temp.pop()
        generate(ans, temp, ind + 1, target, nums) 

    ans = []
    generate(ans, [], 0, target, nums)
    return ans
# T(n) = O(2^n)

# Approach: Sort the array. Then add only those elements
#           which are needed to temp. Once equal to target,
#           append to answer array.
def combinationSumOptimal(nums, target):
    ans = []
    ds = []
    nums.sort()


    def findCombination(ind: int, target: int):
        if target == 0:
            ans.append(ds[:])
            return
        for i in range(ind, len(nums)):
            if i > ind and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            ds.append(nums[i])
            findCombination(i + 1, target - nums[i])
            ds.pop()


    findCombination(0, target)
    return ans
# T(n) = O(2^n)



nums = [2, 5, 2, 1, 2]
target = 5

print(combinationSumBruteForce(nums, target))
print(combinationSumOptimal(nums, target))