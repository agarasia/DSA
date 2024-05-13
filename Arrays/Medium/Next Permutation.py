def nextPermutation(nums):
    n = len(nums)

    # Find the breakpoint
    breakPoint = -1
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            breakPoint = i
            break
    
    # If breakpoint does not exist,
    # reverse the entire array and return
    if breakPoint == -1:
        nums = nums.reverse()
        return nums
    
    # If breakpoint exists,
    # find the next biggest element and swap it
    for i in range(n-1, breakPoint, -1):
        if nums[i] > nums[breakPoint]:
            nums[i], nums[breakPoint] = nums[breakPoint], nums[i]
            break

    # Reverse the rest of the array and return the array
    nums[breakPoint+1:] = reversed(nums[breakPoint+1:])

    return nums

nums = [1, 1, 5]
print(nextPermutation(nums))