def subarrayWithXORBruteForce(nums, target):
    count = 0
    n = len(nums)

    for i in range(n):
        xor = 0
        for j in range(i, n):
            xor ^= nums[j]
            if xor == target:
                count += 1

    return count 

def subarrayWithXOROptimal(nums, target):
    n = len(nums)
    xor = 0
    count = 0
    hashMap = {}
    hashMap[xor] = 1

    for i in range(n):
        xor ^= nums[i]
        prefixXor = xor ^ target
        
        if prefixXor in hashMap:
            count += hashMap[prefixXor]
    
        if xor in hashMap:
            hashMap[xor] += 1
        else:
            hashMap[xor] = 1
    
    return count

nums = [4, 2, 2, 6, 4]
xor = 6

print(subarrayWithXORBruteForce(nums, xor))
print(subarrayWithXOROptimal(nums, xor))