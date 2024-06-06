class Node:
    def __init__(self, val:int) -> None:
        self.data = val
        self.next = None

class LL:
    def __init__(self, head = None) -> None:
        self.head = head

    def append(self, newNode:Node):
        if not self.head:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
    
    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print()

    # Approach: From the existence of loops, we 
    #           can leverage how far the start of the loop
    #           is from the start of the list.
    def loopPosition(self):
        if not self.head or not self.head.next:
            return None
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if not fast or not fast.next:
            return None
        else:
            slow = self.head
            index = 0

            while slow != fast:
                slow = slow.next
                fast = fast.next
                index += 1
        
        return index
    # T(n) = O(n)

ll = LL()
ll.append(Node(3))
n2 = Node(2)
ll.append(n2)
ll.append(0)
n4 = Node(4)
ll.append(n4)
n4.next = n2
print(ll.loopPosition())