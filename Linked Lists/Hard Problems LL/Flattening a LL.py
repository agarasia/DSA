class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.bottom = None

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
            temp = curr
            while temp:
                print(temp.val, end=" -> ")
                temp = temp.bottom
            print()
            curr = curr.next
        print()
    
    def flattenBruteForce(self):
        aux = []
        curr = self.head

        while curr:
            temp = curr
            while temp:
                aux.append(temp.val)
                temp = temp.bottom
            curr = curr.next

        aux = sorted(aux)

        ans = Node(0)
        curr = ans

        for i in aux:
            temp = Node(i)
            curr.next = temp
            curr = curr.next
        
        self.head = ans.next
        

ll = LL()
n1 = Node(5)
n2 = Node(10)
n3 = Node(19)
n4 = Node(28)

n1.bottom = Node(7)
n1.bottom.bottom = Node(8)
n1.bottom.bottom.bottom = Node(30)
n2.bottom = Node(20)
n3.bottom = Node(22)
n3.bottom.bottom = Node(50)
n4.bottom = Node(35)
n4.bottom.bottom = Node(40)
n4.bottom.bottom.bottom = Node(45)

ll.append(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)
ll.print()
ll.flattenBruteForce()
ll.print()
