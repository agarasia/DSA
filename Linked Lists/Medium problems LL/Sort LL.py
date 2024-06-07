class Node:
    def __init__(self, data) -> None:
        self.data = data
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
            print(curr.data, end=" -> ")
            curr = curr.next
        print()

    # Approach: Append all nodes to a list, sort
    #           the list and then update the LL.
    def sort(self):
        aux = []
        curr = self.head

        while curr:
            aux.append(curr.data)
            curr = curr.next

        aux.sort()
        curr = self.head
        
        for i in aux:
            curr.data = i
            curr = curr.next

ll = LL()
ll.append(Node(1))
ll.append(Node(3))
ll.append(Node(2))
ll.append(Node(-1))
ll.print()
ll.sort()
ll.print()
