# Approach: Linearly check if the number is a square root or not.
def rootBruteForce(nums):
    if nums >= 0 and nums <=1:   return nums
    ans = 1
    for i in range(1,nums//2+1):
        if nums >= i*i:
            ans = i
    
    return ans
# T(n) = O(n//2)

# Approach: Use Binary Search to find the lower bound of the root.
def rootOptimal(nums):
    if nums >=0 and nums <= 1:  return nums
    low, high = 1, nums//2
    ans = 1

    while low <= high:
        mid = low + (high-low)//2
        if mid*mid == nums:
            return mid
        if mid*mid <= nums:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return ans
# T(n) = O(log n)

nums = 5

print(rootBruteForce(nums), rootOptimal(nums))