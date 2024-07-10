# Approach: Find all possible sums and 
#           find the max combinations.
def maxCombinationsBruteForce(A, B, C):
    ans = []

    for i in A:
        for j in B:
            ans.append(i+j)
    
    ans.sort(reverse=True)
    return ans[:C]
# T(n) = O(n**2)
# S(n) = O(n)

# Approach: Use a max heap to keep only the 
#           max sums.
def maxCombinationsOptimal(A, B, C):
    def heapify(nums, index):
        max_index = index
        left, right = 2*index+1, 2*index+2

        if left < len(nums) and nums[left] > nums[max_index]:
            max_index = left
        if right < len(nums) and nums[right] > nums[max_index]:
            max_index = right
        
        if max_index != index:
            nums[index], nums[max_index] = nums[max_index], nums[index]
            heapify(nums, max_index)
    
    def insert(nums, val):
        nums.append(val)
        index = len(nums) - 1
        while index and nums[index] > nums[(index-1)//2]:
            nums[index], nums[(index-1)//2] = nums[(index-1)//2], nums[index]
            index = (index-1)//2
    
    def pop(heap):
        top = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        heapify(heap, 0)
        return top

    A.sort(reverse=True)
    B.sort(reverse=True)

    heap = []

    insert(heap, ((A[0] + B[0]), (0, 0)))
    visited = set((0, 0))

    result = []

    for _ in range(C):
        val, (i, j) = pop(heap)
        result.append(val)

        if i+1 < len(A) and (i+1, j) not in visited:
            insert(heap, (A[i+1]+B[j], (i+1, j)))
        
        if j+1 < len(B) and (i, j+1) not in visited:
            insert(heap, (A[i]+B[j+1], (i, j+1)))
    
    return result
# T(n) = O(n logn)
# S(n) = O(C)


A, B, C = [3, 2], [1, 4], 2
print(maxCombinationsBruteForce(A, B, C))
print(maxCombinationsOptimal(A, B, C))