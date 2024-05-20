# Approach: Manually check for all possible inversions
def inversionsBruteForce(nums):
    n = len(nums)
    count = 0

    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                count += 1
            else:
                continue
    
    return count

# Approach: take help from mergeSort's merging step
def inversionsOptimal(nums):
    def merge(nums, low, mid, high):
        left, right = low, mid + 1
        temp = []
        count = 0

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                count += mid - left + 1
                right += 1

        while left <= mid:
            temp.append(nums[left])
            left += 1
        
        while right <= high:
            temp.append(nums[right])
            right += 1

        for i in range(low, high + 1):
            nums[i] = temp[i - low]
        return count

    def mergeSort(nums, low, high):
        count = 0
        if low < high:
            mid = low + (high-low)//2
            count += mergeSort(nums, low, mid)
            count += mergeSort(nums, mid+1, high)
            count += merge(nums, low, mid, high)
        
        return count
    return mergeSort(nums, 0, len(nums)-1)

nums = [5,4,3,2,1]
print(inversionsBruteForce(nums))
print(inversionsOptimal(nums))