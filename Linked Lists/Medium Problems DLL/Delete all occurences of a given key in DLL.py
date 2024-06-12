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
    
    # Approach: Traverse the LL and whenever we reach the
    #           occurence, we manipulate the links of its previous
    #           and the next node.
    def deleteAllOccurences(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                if curr == self.head:
                    self.head = curr.next
                    curr.next.prev = None
                else:
                    prevNode = curr.prev
                    if curr.next:
                        prevNode.next = curr.next
                        curr.next.prev = prevNode
                    else:
                        prevNode.next = None
                    
            curr = curr.next

        return self.head
    # T(n) = O(n)   where n = length of DLL

dll = DLL()
dll.append(Node(9))
dll.append(Node(1))
dll.append(Node(3))
dll.append(Node(4))
dll.append(Node(5))
dll.append(Node(1))
dll.append(Node(8))
dll.append(Node(4))
dll.print()

dll2 = DLL()
dll2.head = dll.deleteAllOccurences(9)
dll2.print()