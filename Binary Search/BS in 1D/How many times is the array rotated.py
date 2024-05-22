# Approach: Find min of array by linear search,
#           then find its position in the array.
def rotatedNTimesBruteForce(nums):
    Min = nums[0]
    for i in nums:
        Min = min(Min, i)
    
    for j in range(len(nums)):
        if nums[j] == Min:
            return j
# T(n) = O(2*n)

# Approach: Use Binary search to find the min element,
#           then use binary search to its position.
def rotatedNTimesOptimal(nums):
    def findMin():
        low, high = 0, len(nums) - 1
        ans = float('inf')

        while low <= high:
            mid = low + (high-low)//2
            if nums[low] <= nums[high]:
                ans = min(ans, nums[low])
                high = mid - 1
            if nums[mid] <= nums[high]:
                ans = min(ans, nums[mid])
                high = mid - 1
            else:
                ans = min(ans, nums[high])
                low = mid + 1
        
        return ans
    
    def search(target):
        low, high = 0, len(nums)-1

        while low <= high:
            mid = low + (high-low)//2

            if nums[mid] == target:
                return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

    Min = findMin()
    return search(Min)
# T(n) = O(2*logn)

nums = [2,3,4,5,1]
print(rotatedNTimesBruteForce(nums))
print(rotatedNTimesOptimal(nums))