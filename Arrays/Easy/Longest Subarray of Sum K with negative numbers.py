def maxLenOfSumK(arr, k):
    hash_map = {}
    max_len = 0
    sum = 0

    for i in range(len(arr)):
        sum += arr[i]

        if sum == k:
            max_len = max(max_len, i + 1)
        
        rem = sum - k

        if rem in hash_map:
            max_len = max(max_len, i - hash_map[rem])
        
        if rem not in hash_map:
            hash_map[rem] = i
    
    return max_len

arr = [-1, -3, 4, 0, 2, -3, 4]
k = 0
print(maxLenOfSumK(arr, k))