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

def reverse(head):
    curr = head
    prev = None

    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    
    return prev

def addOne(head):
    head = reverse(head)          # reversing list to make addition easy
    
    current = head
    carry = 1
    
    while(carry):
        current.data += 1         # adding one to current node
        
        if current.data < 10:
            return reverse(head)
            # if no carry we can reverse back list and return it
        else:
            current.data = 0
            # else we continue with taking carry forward
        
        if current.next is None:
            break
            # if end of list, we break from loop
        else:
            current = current.next
            # else we move to next node
    
    current.next = Node(1)        # adding new node for the carried 1
    return reverse(head)


ll = LL()
ll.append(Node(9))
ll.append(Node(9))
ll.append(Node(9))
ll.append(Node(9))

ll.print()
h = addOne(ll.head)
while h:
    print(h.data, end=" -> ")
    h = h.next