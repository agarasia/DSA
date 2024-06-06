# Initializing Nodes of linked list
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Initializing LinkedList comprising of Nodes
class LinkedList:
    def __init__(self, head:Node):
        self.head = head
    
    def insertAtFront(self, newNode:Node):
        newHead = newNode
        newHead.next = self.head
        self.head = newHead

        return self.head
    
    def insertAtBack(self, newNode:Node):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode

        return self.head

    # Helper Print function
    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next

n1 = Node(1)
n2 = Node(2)
ll = LinkedList(n1)
ll.print()
print()
ll.insertAtFront(n2)
ll.insertAtFront(Node(12))
ll.print()
print()
ll.insertAtBack(Node(21))
ll.print()