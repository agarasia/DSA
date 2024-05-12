import sys

def maxSumSubarray(arr):
    n = len(arr)
    maxSum = -sys.maxsize - 1
    ansStart, ansEnd = -1, -1
    sum = 0
    start = 0
    ans = []

    for i in range(n):
        if sum == 0:    start = i

        if sum > maxSum:
            maxSum = sum
            ansStart = start
            ansEnd = i
        
        sum += arr[i]

        if sum < 0:     sum = 0

    for i in range(ansStart, ansEnd):
        ans.append(arr[i])  

    return ans 

a = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSumSubarray(a))