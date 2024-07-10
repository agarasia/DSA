def isPossible(hand, k):
    def heapify(nums, index):
        min_index = index
        left, right = 2*index+1, 2*index+2

        if left < len(nums) and nums[left] < nums[min_index]:
            min_index = left
        if right < len(nums) and nums[right] < nums[min_index]:
            min_index = right
        
        if min_index != index:
            nums[min_index], nums[index] = nums[index], nums[min_index]
            heapify(nums, min_index)
    
    def buildHeap(nums):
        for i in range(len(nums) // 2 - 1, -1, -1):
            heapify(nums, i)
    
    def getMin(nums):
        return nums[0]
    
    def delete(nums):
        nums[0] = nums[-1]
        nums.pop()
        heapify(nums, 0)
    

    if len(hand) % k:
        return False
    
    # Main Program
    count = {}
    for i in hand:
        count[i] = count.get(i, 0) + 1
    
    minHeap = list(count.keys())
    buildHeap(minHeap)
    while minHeap:
        first = getMin(minHeap)

        for i in range(first, first + k):
            if i not in count:
                return False
            
            count[i] -= 1
            if count[i] == 0:
                if i != minHeap[0]:
                    return False
                delete(minHeap)
    
    return True
# T(n) = O(n * logn)
# S(n) = O(n)
            


hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3

print(isPossible(hand, groupSize))