# Approach: Find all possible triplets
def threeSumBruteForce(nums):
    n = len(nums)
    st = set()

    # Find all possible triplets and append to set.
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (nums[i] + nums[j] + nums[k]) == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    st.add(tuple(temp))
    return [list(i) for i in st]

# Approach: Use a hashset to reduce the number of for loops
def threeSumBetter(nums):
    n = len(nums)
    st = set()

    # Initialize a for loop
    for i in range(n):
        hashSet = set()
        for j in range(i+1, n):
            third = -(nums[i] + nums[j])
            if third in hashSet:
                temp = [nums[i], nums[j], third]
                temp.sort()
                st.add(tuple(temp))
            hashSet.add(nums[j])
    
    return [list(i) for i in st]

def threeSumOptimal(nums):
    n = len(nums)
    ans = []
    nums.sort()
    
    for i in range(n):
        if i != 0 and nums[i] == nums[i-1]:
            continue

        j = i + 1
        k = n - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                temp = [nums[i], nums[j], nums[k]]
                ans.append(temp)
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
        return ans

nums = [-2,0,1,1,2]
print(threeSumBruteForce(nums), threeSumBetter(nums), threeSumOptimal(nums))