def longestConsecutiveSequenceNaive(nums):
    n = len(nums)
    if n == 0:  return 0                # Edge case: empty array

    nums.sort()                         # Sort the array, and find
    lastSmaller = float('-inf')         # the longest consecutive
    count = 0                           # sequence
    longest = 1

    # Run a for loop and check if consecutive elements are there
    for i in range(n):
        if nums[i] == lastSmaller + 1:
            count += 1
            lastSmaller = nums[i]
        elif nums[i] != lastSmaller:
            count = 1
            lastSmaller = nums[i]
        longest = max(longest, count)
    
    return longest

def longestConsecutiveSequenceOptimal(nums):
    # Use Set data structure
    n = len(nums)
    if n == 0:  return 0                # Edge case: empty array

    longest = 1
    st = set()
    for i in range(n):
        st.add(nums[i])

    for i in st:
        if i-1 not in st:
            count = 1
            x = i
            while x + 1 in st:
                x += 1
                count += 1
            longest = max(longest, count)
    return longest

nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutiveSequenceOptimal([0,3,7,2,5,8,4,6,0,1]), longestConsecutiveSequenceNaive([0,3,7,2,5,8,4,6,0,1]))