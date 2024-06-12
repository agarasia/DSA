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

    # Approach: Just traverse to the next distinct node
    #           and connect it to current node.
    def deleteDuplicates(self):
        curr = self.head

        while curr and curr.next:
            nextNode = curr.next

            while nextNode and curr.data == nextNode.data:
                duplicate = nextNode
                nextNode = nextNode.next
                del duplicate
            
            curr.next = nextNode
            if nextNode:
                nextNode.prev = curr
            
            curr = curr.next
    # T(n) = O(n)   where n = length of the DLL
        
        
dll = DLL()
dll.append(Node(1))
dll.append(Node(1))
dll.append(Node(1))
dll.append(Node(2))
dll.append(Node(2))
dll.append(Node(2))
dll.append(Node(3))
dll.print()
dll.deleteDuplicates()
dll.print()