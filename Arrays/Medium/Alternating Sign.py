def alternatingArrayNaive(nums):
    pos, neg = [], []

    for i in nums:
        if i > 0:   pos.append(i)
        else:       neg.append(i)
    
    pos_count, neg_count = 0, 0
    for i in range(len(nums)):
        if i % 2 == 0:
            nums[i] = pos[pos_count]
            pos_count += 1
        else:
            nums[i] = neg[neg_count]
            neg_count += 1

    return nums

def alternatingArrayOptimal(nums):
    pos_index, neg_index = 0, 1
    curr_index = 0
    while pos_index < len(nums) and neg_index < len(nums):
        if nums[curr_index] > 0:
            nums[pos_index], nums[curr_index] = nums[curr_index], nums[pos_index]
            pos_index += 2
        else:
            nums[neg_index], nums[curr_index] = nums[curr_index], nums[neg_index]
            neg_index += 2
        curr_index += 1
    
    return nums


a = [3,1,-2,-5,2,-4]
print(alternatingArrayOptimal(a))