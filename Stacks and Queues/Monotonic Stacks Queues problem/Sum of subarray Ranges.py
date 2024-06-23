def sumOfRangesBruteForce(nums):
    ans = 0

    for i in range(len(nums)):
        Max, Min = nums[i], nums[i]
        for j in range(i, len(nums)):
            Min = min(Min, nums[j])
            Max = max(Max, nums[j])
            ans += (Max - Min)
    
    return ans

def sumOfRangesOptimal(A0):
    res = 0
    inf = float('inf')
    A = [-inf] + A0 + [-inf]
    s = []
    for i, x in enumerate(A):
        while s and A[s[-1]] > x:
            j = s.pop()
            k = s[-1]
            res -= A[j] * (i - j) * (j - k)
        s.append(i)
        
    A = [inf] + A0 + [inf]
    s = []
    for i, x in enumerate(A):
        while s and A[s[-1]] < x:
            j = s.pop()
            k = s[-1]
            res += A[j] * (i - j) * (j - k)
        s.append(i)
    return res

nums = [4,-2,-3,4,1]
print(sumOfRangesBruteForce(nums))
print(sumOfRangesOptimal(nums))