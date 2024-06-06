# Initializing Node for a doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
# Initializing Linked List class
class LinkedList:
    def __init__(self, head=None):
        self.head = head

# Function to implement a 2D Linked List
# for a given list.
def constructLL(arr):
    ll = LinkedList()
    head = Node(arr[0])
    ll.head = head

    for i in range(1, len(arr)):
        tempNode = Node(arr[i])
       
        tempNode.prev = head
        head.next = tempNode

        head = head.next
    
    return ll.head

arr = [1,2,3,4,5]
head = constructLL(arr)
while head:
    print(head.data,end=" <-> ")
    head = head.next
print()