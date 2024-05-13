def leaders(nums):
    n = len(nums)
    ans = [nums[-1]]    # Last element is always a leader
    
    # Find possible leader elements from the end of the array
    for i in range(n-2, -1, -1):
        if nums[i] >= ans[-1]:
            ans.append(nums[i])
    
    # Reverse the array, and return it
    ans = reversed(ans)

    return list(ans)

nums = [16, 17, 4, 3, 5, 2]
print(leaders(nums), leaders([1,2,3,4,0]))