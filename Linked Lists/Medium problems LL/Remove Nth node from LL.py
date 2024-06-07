# Initializing nodes for linked list
class Node:
    def __init__(self, val:int) -> None:
        self.data = val
        self.next = None

# Initializing Linked List
class LL:
    def __init__(self, head = None) -> None:
        self.head = None

    def append(self, newNode:int):
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

    # Approach: traverse the list to find its length
    #           and then remove (length - n)th node.
    def removeNthFromEnd(self, n):
        # Edge case: Singular linked list
        if not self.head.next:
            return None
        
        # Finding the length
        length, curr = 0, self.head
        while curr:
            length += 1
            curr = curr.next

        # Edge Case: Removing head element
        if length == n:
            return self.head.next

        # Removing (length-n)th node
        length -= n
        curr = self.head

        while (length - 1):
            length -= 1
            curr = curr.next

        if curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None

        return self.head
# T(n) = O(2*n)

ll = LL()
ll.append(Node(1))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(4))
ll.append(Node(5))
ll.append(Node(6))
ll.append(Node(7))
# ll.print()
head = ll.removeNthFromEnd(2)
while head:
    print(head.data, end=" -> ")
    head = head.next