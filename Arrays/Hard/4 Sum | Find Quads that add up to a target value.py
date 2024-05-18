# Approach: Find all possible quads and check if they add up to target.
def fourSumBruteForce(nums, target):
    st = set()
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        st.add(tuple(temp))
    
    return [list(i) for i in st]
    # T(n) : O(n ** 4)

# Approach: Use a hash set to reduce the number of for loops to 3.
def fourSumBetter(nums, target):
    n = len(nums)
    st = set()

    for i in range(n):
        for j in range(i+1, n):
            hashSet = set()
            for k in range(j+1, n):
                sum = nums[i] + nums[j] + nums[k]
                rem = target - sum
                if rem in hashSet:
                    temp = [nums[i], nums[j], nums[k], rem]
                    temp.sort()
                    st.add(tuple(temp))
                hashSet.add(nums[k])
    
    return [list(i) for i in st]
    # T(n) = O(n**3  + nlogn)

# Approach: Similar to 3 sum, remove the use of set and hash set.
def fourSumOptimal(nums, target):
    n = len(nums) # size of the array
    ans = []

    # sort the given array:
    nums.sort()

    # calculating the quadruplets:
    for i in range(n):
        # avoid the duplicates while moving i:
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            # avoid the duplicates while moving j:
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # 2 pointers:
            k = j + 1
            l = n - 1
            while k < l:
                _sum = nums[i] + nums[j] + nums[k] + nums[l]
                if _sum == target:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    ans.append(temp)
                    k += 1
                    l -= 1

                    # skip the duplicates:
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
                elif _sum < target:
                    k += 1
                else:
                    l -= 1

    return ans
    # T(n) = O(n**2)



nums = [2,2,2,2,2,2]
target = 8

print(fourSumBruteForce(nums, target))
print(fourSumBetter(nums, target))
print(fourSumOptimal(nums, target))