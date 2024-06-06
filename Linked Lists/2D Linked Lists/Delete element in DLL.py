class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, head = None) -> None:
        self.head = head

    def append(self, newNode:Node):
        if not self.head:
            self.head = newNode
        else:
            currNode = self.head
            
            while currNode.next:
                currNode = currNode.next
            
            newNode.prev = currNode
            currNode.next = newNode

    def print(self):
        currNode = self.head
        while currNode:
            print(currNode.data, end=" <-> ")
            currNode = currNode.next
        print()

    def insertAtPosition(self, newNode, p):
        curr = self.head
        current = 1

        while current < p - 1:
            curr = curr.next
            current += 1
        
        nextNode = curr.next
        curr.next = newNode
        newNode.next = nextNode
        newNode.prev = curr
        nextNode.prev = newNode

    # Delete a node at given position
    def deleteNode(self, position):
        if self.head is None or position < 0:
            return
        
        current = self.head

        # If the node to be deleted is the head node
        if position == 0:
            self.head = current.next
            if self.head:
                self.head.prev = None
            current = None
            return

        # Find the node to be deleted
        for i in range(position):
            current = current.next
            if current is None:
                return
        
        if current.next:
            current.next.prev = current.prev

        if current.prev:
            current.prev.next = current.next

        current = None 

ll = LinkedList()
ll.append(Node(1))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(4))
ll.append(Node(5))
ll.append(Node(6))
ll.print()
ll.insertAtPosition(Node(12), 5)
ll.print()