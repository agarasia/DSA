def countNGEs(nums, queries, indices):
    ans = []
        
    for i in range(queries):
        val = nums[indices[i]]
        count = 0
        for j in range(indices[i], len(nums)):
            if nums[j] > val:
                count += 1
        ans.append(count)
    
    return ans


nums = [3, 4, 2, 7, 5, 8, 10, 6]
queries = 2
indices = [0, 5]

print(countNGEs(nums, queries, indices))