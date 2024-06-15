def possibleSums(nums):
    def generate(ans, temp, ind, nums):
        if ind == len(nums):
            ans.append(temp)
            return
        
        generate(ans, temp + nums[ind], ind + 1, nums)
        generate(ans, temp, ind + 1, nums)

    if not nums:
        return [0]
    
    ans = []
    generate(ans, 0, 0, nums)
    return ans

nums = [2, 3]
print(possibleSums(nums))