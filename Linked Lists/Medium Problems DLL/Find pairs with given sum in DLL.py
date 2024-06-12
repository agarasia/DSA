class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.prev = None
        self.next = None

class DLL:
    def __init__(self, head = None) -> None:
        self.head = head

    def append(self, newNode):
        if not self.head:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
            newNode.prev = curr
    
    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print()

    # Approach: Keep track of all elements in a hashmap and 
    #           if difference is already in the hashmap, then
    #           append the pair in the ans.
    def pairsBruteForce(self, target):
        ans = []
        hashMap = {}
        curr = self.head
        index = 0

        while curr:
            hashMap[curr.data] = index
            diff = target - curr.data
            if diff in hashMap and hashMap[diff] != index:
                ans.append([diff, curr.data])
            
            curr = curr.next
            index += 1
        
        return sorted(ans)
    # T(n) = O(n) where n = length of the DLL
    # S(n) = O(n) for storing keys in hashMap

    # Approach: Since the DLL is sorted, we can exploit this
    #           and traverse the DLL in both ways, thus optimizing
    #           the space complexity.
    def pairsOptimal(self, target):
        ptr1, ptr2 = self.head, self.head
        ans = []

        # Traverse to the end
        while ptr2.next:
            ptr2 = ptr2.next

        while ptr1 != ptr2 and ptr2.next != ptr1:
            total = ptr1.data + ptr2.data

            if total == target:
                ans.append([ptr1.data, ptr2.data])
                ptr1 = ptr1.next
                ptr2 = ptr2.prev
            
            elif total > target:
                ptr2 = ptr2.prev
            
            else:
                ptr1 = ptr1.next

        return ans
    # T(n) = O(2*n) where n = length of DLL

dll = DLL()
dll.append(Node(1))
dll.append(Node(2))
dll.append(Node(4))
dll.append(Node(5))
dll.append(Node(6))
dll.append(Node(8))
dll.append(Node(9))
dll.print()

print(dll.pairsBruteForce(10))
print(dll.pairsOptimal(10))