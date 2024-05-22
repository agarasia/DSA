# Approach: Use xor operation to find the singular element
def singularBruteForce(nums):
    xor = 0
    for i in nums:
        xor ^= i
    return xor

# Approach: 
# def singularOptimal(nums):

nums = [1,1,2,3,3,4,4,5,5,8,8]
print(singularBruteForce(nums))