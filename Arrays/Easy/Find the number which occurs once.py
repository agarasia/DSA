def missing1(nums):
    missing = nums[0]
    for i in range(1, len(nums)):
        missing = missing ^ nums[i]
        # print(missing)
    return missing

nums = [1, 1, 2, 3, 3, 4, 4]
print(missing1(nums))