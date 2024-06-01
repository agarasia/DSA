# Approach: Append into one, sort  the
#           array and return the kth element.
def kthElementBruteForce(nums1, nums2, k):
    for i in nums2:
        nums1.append(i)
    
    nums1.sort()

    return nums1[k-1]
# T(n) = (len(nums1)+len(nums2)) log (len(nums1)+len(nums2))

# Approach: Traverse both arrays till we find
#           the kth element.
def kthElementBetter(nums1, nums2, k):
    n1, n2 = len(nums1), len(nums2)
    count = 0
    i, j = 0, 0

    while i < n1 and j < n2:
        if nums1[i] < nums2[j]:
            if count == k:
                return nums1[i]
            count += 1
            i += 1
        else:
            if count == k:
                return nums2[j]
            count += 1
            j += 1
    
    while i < n1:
        if count == k:
            return nums1[i]
        count += 1
        i += 1
    
    while j < n2:
        if count == k:
            return nums2[j]
        count += 1
        j += 1
# T(n) = O(len(nums1) + len(nums2))

# Approach: Use Binary Search to optimize the
#           searching process.
def kthElementOptimal(nums1, nums2, k):
    n1, n2 = len(nums1), len(nums2)
    
    if n1 > n2:
        return kthElementOptimal(nums2, nums1, k)
    
    left = k

    low, high = max(0, k - n2), min(k, n1)

    while low <= high:
        mid1 = low + (high - low)//2
        mid2 = left - mid1

        l1, l2 = float('-inf'), float('-inf')
        r1, r2 = float('inf'), float('inf')

        if mid1 < n1:
            r1 = nums1[mid1]
        if mid2 < n2:
            r2 = nums2[mid2]
        if mid1 - 1 >= 0:
            l1 = nums1[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = nums2[mid2 - 1]

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)

        # eliminate the halves:
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1

    return 0  # dummy statement

nums1, nums2 = [2, 3, 45], [4, 6, 7, 8]
k = 4

print(kthElementBruteForce(nums1, nums2, k))
print(kthElementBetter(nums1, nums2, k))
print(kthElementOptimal(nums1, nums2, k))