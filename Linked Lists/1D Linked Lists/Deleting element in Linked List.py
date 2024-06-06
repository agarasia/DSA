class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self, head = None) -> None:
        self.head = None
    
    def append(self, newNode:Node):
        if not self.head:
            self.head = newNode
        else:
            curr = self.head

            while curr.next:
                curr = curr.next
                
            curr.next = newNode
    
    def deleteNode(self, key:int):
        if self.head.data == key:
            self.head = self.head.next
        else:
            currNode = self.head

            while currNode.next.data != key:
                currNode = currNode.next

            currNode.val = currNode.next.data
            currNode.next = currNode.next.next

    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next


n1 = Node(1)
ll = LinkedList()
ll.append(n1)
ll.append(Node(2))
ll.append(Node(3))
ll.print()
print()
ll.deleteNode(1)
ll.print()