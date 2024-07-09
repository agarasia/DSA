# Approach: Take an auxiliary array and a hashmap. Sort 
#           the auxiliary array and note down the ranks
#           for them in a hashMap. Replace their ranks with
#           the key values.
def ranks(nums):
    hashMap = {}
    ans = []
    
    for i in nums:
        ans.append(i)
    
    ans.sort()
    rank = 1
    for i in range(len(nums)):
        hashMap[ans[i]] = rank
        if i+1 < len(nums) and nums[i] == nums[i+1]:
            continue
        rank += 1
    
    for i in range(len(nums)):
        nums[i] = hashMap[nums[i]]

    return nums
# T(n) = O(nlogn)
# S(n) = O(n)

nums = [20, 15, 26, 2, 98, 6]

print(ranks(nums))