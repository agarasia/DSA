def reversePairsBruteForce(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > 2*nums[j]:
                count += 1
            else:   continue
    return count

def reversePairsOptimal(nums):
    def merge(nums, low, mid, high):
        left, right = low, mid + 1
        temp = []

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        while left <= mid:
            temp.append(nums[left])
            left += 1
        
        while right <= high:
            temp.append(nums[right])
            right += 1

        for i in range(low, high + 1):
            nums[i] = temp[i - low]

    def countPairs(nums, low, mid, high):
        right = mid + 1
        count = 0
        
        for i in range(low, mid + 1):
            while right <= high and nums[i] > 2*nums[right]:
                right += 1
            count += (right - (mid + 1))
        
        return count

    def mergeSort(nums, low, high):
        count = 0
        if low < high:
            mid = low + (high-low)//2
            count += mergeSort(nums, low, mid)
            count += mergeSort(nums, mid+1, high)
            count += countPairs(nums, low, mid, high)
            merge(nums, low, mid, high)
        
        return count
    
    return mergeSort(nums, 0, len(nums)-1)

nums = [1, 3, 2, 3, 1]
print(reversePairsBruteForce(nums))
print(reversePairsOptimal(nums))