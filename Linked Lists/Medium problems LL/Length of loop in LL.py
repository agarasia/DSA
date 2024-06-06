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
    def loopLength(self):
        slow = fast = self.head
        count=1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                while slow.next!=fast:
                    slow=slow.next
                    count+=1
                return count
        else:
            return 0

ll = LL()
ll.append(Node(3))
n2 = Node(2)
ll.append(n2)
ll.append(0)
n4 = Node(4)
ll.append(n4)
n4.next = n2
print(ll.loopLength())