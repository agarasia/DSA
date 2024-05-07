def maxArrayWithSumK(arr, k):
    # Brute Force
    # max_len = 0
    # for i in range(0, len(arr)):
    #     sum = 0
    #     for j in range(i, len(arr)):
    #         sum += arr[j]
    #         if sum == k:
    #             max_len = max(max_len, j - i + 1)
    
    # return max_len

    # Optimal
    left, right = 0, 0
    sum = arr[0]
    max_len = 0

    while right < len(arr):
        while left <= right and sum > k:
            sum -= arr[left]
            left += 1
        
        if sum == k:
            max_len = max(max_len, right - left + 1)
        
        right += 1
        if right < len(arr): sum += arr[right]
    
    return max_len

arr = [1, 2, 3, 1, 1, 1, 1]
arr2 = [1,2,1,3]
k = 3
print(maxArrayWithSumK(arr2, 2))