class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LL:
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
    
    def print(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print()

    def rotate(self, k):
        def length():
            curr = self.head
            len = 1
            while curr.next:
                len += 1
                curr = curr.next
            return len
        
        k = k % length()
        steps = length() - k

        lastNode = self.head
        headNode = self.head

        while lastNode.next:
            lastNode = lastNode.next
        
        lastNode.next = self.head

        while steps-1:
            headNode = headNode.next
            steps -= 1
        
        self.head = headNode.next
        headNode.next = None
        
        


ll = LL()
ll.append(Node(0))
ll.append(Node(1))
ll.append(Node(2))
ll.print()
print(ll.rotate(4))
ll.print()