def oddOccurencesOptimal(nums):
    xor2 = nums[0]
    x, y = 0, 0

    for i in range(1, len(nums)):
        xor2 = xor2 ^ nums[i]
    
    set_bit_no = xor2 & ~(xor2 - 1)

    for i in range(len(nums)):
        if nums[i] & set_bit_no:
            x ^= nums[i]
        else:
            y ^= nums[i]
    
    v = [max(x, y), min(x, y)]
    return v
# T(n) = O(n)   where n = length of nums
# S(n) = O(1)

# Approach: Create a hashmap and hash the array.
#           There will be only 2 elements which would
#           have odd number occurences which could be recorded
#           and returned in a decreasing order.
def oddOccurencesBruteForce(nums):
    hashMap = {}
    ans = []
    for i in nums:
        if i not in hashMap:
            hashMap[i] = 1
        else:
            hashMap[i] += 1
    
    for i in hashMap:
        if hashMap[i]%2 == 1:
            ans.append(i)
    
    ans.sort(reverse=True)

    return ans    
# T(n) = O(n)   where n = length of nums
# S(n) = O(n)   to store the hashMap

nums = [4, 2, 4, 5, 2, 3, 3, 1]
print(oddOccurencesBruteForce(nums))
print(oddOccurencesOptimal(nums))