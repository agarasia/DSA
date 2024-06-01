# Approach: Merge both arrays and find the median.
def medianBruteForce(nums1, nums2):
    for i in nums2:
        nums1.append(i)
    
    nums1.sort()
    
    n = len(nums1)
    if n % 2:   return nums1[n//2]
    return (nums1[n//2] + nums1[n//2 - 1])/2
# T(n) = O((len(nums1) + len(nums2)) log (len(nums1) + len(nums2)))
    
def medianBetter(a, b):
    # size of two given arrays:
    n1, n2 = len(a), len(b)
    n = n1 + n2  # total size
    # required indices:
    ind2 = n // 2
    ind1 = ind2 - 1
    cnt = 0
    ind1el, ind2el = -1, -1

    # apply the merge step:
    i, j = 0, 0
    while i < n1 and j < n2:
        if a[i] < b[j]:
            if cnt == ind1:
                ind1el = a[i]
            if cnt == ind2:
                ind2el = a[i]
            cnt += 1
            i += 1
        else:
            if cnt == ind1:
                ind1el = b[j]
            if cnt == ind2:
                ind2el = b[j]
            cnt += 1
            j += 1

    # copy the left-out elements:
    while i < n1:
        if cnt == ind1:
            ind1el = a[i]
        if cnt == ind2:
            ind2el = a[i]
        cnt += 1
        i += 1
    while j < n2:
        if cnt == ind1:
            ind1el = b[j]
        if cnt == ind2:
            ind2el = b[j]
        cnt += 1
        j += 1

    if n % 2 == 1:
        return float(ind2el)

    return float(ind1el + ind2el) / 2.0


nums1 = [1,2,3]
nums2 = [5,7,9]

print(medianBruteForce(nums1, nums2))
print(medianBetter(nums1, nums2))