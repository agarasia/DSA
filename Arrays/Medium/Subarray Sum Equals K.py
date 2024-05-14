def subarraySumBruteForce(nums, target):
    count = 0

    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum == target:
                count += 1

    return count

nums = [1,1,1]
k = 2
print("Count : ", subarraySumBruteForce(nums, k))