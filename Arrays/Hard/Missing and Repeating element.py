def missingRepeatingBruteForce(nums):
    n = len(nums)
    hashMap = {}
    repeating, missing = 0, 0
    for i in range(n):
        if nums[i] in hashMap:
            hashMap[nums[i]] += 1
        else:
            hashMap[nums[i]] = 1
    
    for i in hashMap:
        if hashMap[i] > 1:
            repeating = i

    idealSum = n*(n+1)//2
    sum = 0

    for i in nums:
        sum += i
    
    diff = abs(sum - idealSum)

    missing = abs(diff - repeating)
    return [repeating, missing]

def missingRepeatingOptimal(nums):
    n = len(nums)
    Sn = (n*(n+1))//2
    S2n = (n*(n+1)*(2*n + 1))//6
    S, S2 = 0, 0

    for i in nums:
        S += i
        S2 += i**2
    
    term1 = S - Sn
    term2 = (S2 - S2n)//term1

    x = (term2 + term1)//2
    y = (term2 - term1)//2

    return [x, y]

nums = [1, 3, 3]
print(missingRepeatingBruteForce(nums))