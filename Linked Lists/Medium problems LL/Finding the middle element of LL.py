class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LL:
    def __init__(self, head = None):
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

    # Approach: initialize two pointers, both of which traverse
    #           the linked list at different speeds. When one 
    #           reaches the end, the other should reach the middle!
    def mid(self):
        if not self.head or not self.head.next:
            return self.head
        else:
            slow, fast = self.head, self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
        
        return slow.data
        


ll = LL()
ll.append(Node(1))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(4))
ll.print()
middle = ll.mid()
print(middle)