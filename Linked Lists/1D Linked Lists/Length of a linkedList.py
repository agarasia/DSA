# Initializing Nodes of linked list
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Initializing LinkedList comprising of Nodes
class LinkedList:
    def __init__(self, head:Node):
        self.head = head

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

    # Main function
    def length(self):
        curr = self.head
        length = 0

        while curr:
            curr = curr.next
            length += 1
        
        return length

    # Helper Print function
    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print()

n1 = Node(1)
n2 = Node(2)
ll = LinkedList(n1)
ll.print()
ll.append(n2)
ll.append(Node(12))
ll.print()
ll.append(Node(21))
ll.print()
print(ll.length())