# Initializing nodes for linked list
class Node:
    def __init__(self, val:int) -> None:
        self.data = val
        self.next = None

# Initializing Linked List
class LL:
    def __init__(self, head = None) -> None:
        self.head = None

    def append(self, newNode:int):
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

    # Approach: traverse the list and keep appending
    #           the odd and then even indexed nodes.
    def oddEvenList(self):
        oddFast, evenFast = self.head, self.head.next
        ans = LL()
        
        # Appending all the odd indexed
        while oddFast and oddFast.next:
            ans.append(Node(oddFast.data))
            oddFast = oddFast.next.next

        if oddFast:
            ans.append(Node(oddFast.data))

        while evenFast and evenFast.next:
            ans.append(Node(evenFast.data))
            evenFast = evenFast.next.next

        if evenFast:
            ans.append(Node(evenFast.data))
        
        return ans.head
    


ll = LL()
ll.append(Node(1))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(4))
ll.append(Node(5))
ll.append(Node(6))
ll.append(Node(7))
# ll.print()
head = ll.oddEvenList()
while head:
    print(head.data, end=" -> ")
    head = head.next