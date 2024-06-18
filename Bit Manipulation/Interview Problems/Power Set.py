def generate(nums):
    n = len(nums)
    res = []

    for i in range(2**n, 2**(n+1)):
        bitmask = bin(i)[3:]

        res.append([nums[j] for j in range(n) if bitmask[j] == "1"])

    return res

nums = [1,2,3]
print(generate(nums))
