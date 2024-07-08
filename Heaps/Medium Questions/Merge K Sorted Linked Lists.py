class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

# Approach: Append all lists to an empty list, 
#           sort it and make it into a LL.
def mergeListsBruteForce(lists):
    # Appending to a List
    temp = []
    for i in range(len(lists)):
        curr = lists[i]
        while curr:
            temp.append(curr.val)
            curr = curr.next
    
    # Sort the array
    temp.sort()

    # Making it an LL
    ans = ListNode(0)
    curr = ans
    for i in temp:
        Temp = ListNode(i)
        curr.next = Temp
        curr = curr.next
    
    return ans.next
# T(n) = O(k*n (logk + logn))
# S(n) = O(k*n)

# Approach: Append to a list; make a min heap;
#           sort it; make it an LL
def mergeListsOptimal1(lists):
    # Helper Functions
    def _heapify(nums, index):
        min_index = index
        left, right = 2*index+1, 2*index+2
        
        if left < len(nums) and nums[min_index] > nums[left]:
            min_index = left
        
        if right < len(nums) and nums[min_index] > nums[right]:
            min_index = right
        
        if min_index != index:
            nums[min_index], nums[index] = nums[index], nums[min_index]
            _heapify(nums, min_index)
    
    def _extractMin(nums):
        if len(nums) == 1:
            return nums.pop()
        result = nums[0]
        nums[0] = nums.pop()
        _heapify(nums, 0)
        return result  
    
    # Main Program
    if not lists or len(lists) == 0:
        return None

    temp = []
    for i in range(len(lists)):
        curr = lists[i]
        while curr:
            temp.append(curr.val)
            curr = curr.next
    
    for i in range((len(temp))//2 - 1, -1, -1):
        _heapify(temp, i)
    
    Sorted = []
    while temp:
        Sorted.append(_extractMin(temp))
    
    head = ListNode(0)
    curr = head
    for i in range(len(Sorted)):
        temp = ListNode(Sorted[i])
        curr.next = temp
        curr = curr.next
    
    return head.next
# T(n) = O(k*n (logk + logn))
# S(n) = O(k*n)

# Approach: Use Merge part of the mergeSort algorithm
def mergeListsOptimal2(lists):
    def _merge(l1, l2):
        merged = ListNode(0)
        curr = merged

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
        
        if l1:
            curr.next = l1
        else:
            curr.next = l2
    
        return merged.next

    if not lists or len(lists) == 0:
        return None
    
    while len(lists) > 1:
        mergedList = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if (i+1) < len(lists) else None
            merged = _merge(l1, l2)
            mergedList.append(merged)
        
        lists = mergedList

    return lists[0]

# ----------------------------------------------------------------------------------------------
l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

lists = [l1, l2, l3]
merged = mergeListsBruteForce(lists)
while merged:
    print(merged.val, end=" -> ")
    merged = merged.next

print()
merged = mergeListsOptimal1(lists)
while merged:
    print(merged.val, end=" -> ")
    merged = merged.next

print()
merged = mergeListsOptimal2(lists)
while merged:
    print(merged.val, end=" -> ")
    merged = merged.next
