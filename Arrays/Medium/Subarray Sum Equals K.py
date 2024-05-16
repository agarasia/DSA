# Approach : Brute Force (Find all possible contiguous subarrays)
def subarraySumBruteForce(nums, target):
    count = 0

    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum == target:
                count += 1

    return count

# Approach : Use a hash map <- optimal
def subarraySumOptimal(nums, target):
    count = 0
    h_map = {0 : 1}     # Adding the key 1 to '0' as there will be
                        # an empty array case.
    Sum = 0
    for i in range(len(nums)):
        Sum += nums[i]      # Keeping track of the prefix sum

        if Sum - target in h_map:   # if remaining sum is in map already,
            count += h_map[Sum - target]
        if Sum in h_map:            # if the prefix sum exists in map
            h_map[Sum] += 1
        else:
            h_map[Sum] = 1
    
    return count

nums = [1,1,1]
k = 2
print("Count : ", subarraySumBruteForce(nums, k), subarraySumOptimal(nums, k))