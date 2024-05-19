def mergeTwoArrraysBruteForce(nums1, m, nums2, n):
    nums3 = [0]*(m+n)
    ptr1, ptr2, = 0, 0
    index = 0

    while ptr1 < m and ptr2 < n:
        if nums1[ptr1] <= nums2[ptr2]:
            nums3[index] = nums1[ptr1]
            index += 1
            ptr1 += 1
        else:
            nums3[index] = nums2[ptr2]
            index += 1
            ptr2 += 1
    
    while ptr1 < m:
        nums3[index] = nums1[ptr1]
        index += 1
        ptr1 += 1
    
    while ptr2 < n:
        nums3[index] = nums2[ptr2]
        index += 1
        ptr2 += 1

    for i in range(m+n):
        nums1[i] = nums3[i]
    

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m, n = 3, 3
mergeTwoArrraysBruteForce(nums1, m, nums2, n)
print(nums1)
