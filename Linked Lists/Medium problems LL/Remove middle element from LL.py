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

    # Approach: Use Tortoise and Hare approach
    #           to find middle element and its previous
    #           element. then remove the middle element.
    def removeMiddleElement(self):
        if not self.head.next:
            return None

        prev = None
        slow, fast = self.head, self.head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        slow = slow.next
        prev.next = slow

        return self.head
# T(n) = O(n)

ll = LL()
ll.append(Node(1))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(4))
ll.append(Node(5))
ll.append(Node(6))
ll.append(Node(7))
# ll.print()
head = ll.removeMiddleElement()
while head:
    print(head.data, end=" -> ")
    head = head.next