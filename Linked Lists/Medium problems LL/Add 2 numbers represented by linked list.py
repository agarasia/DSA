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

# Approach: Reverse the list, keep track of carry throughout
#           the list and then do elementary addition.
def sumOfLL(headA, headB):
    headA, headB = reverse(headA), reverse(headB)
    headC = Node(0)
    curr = headC
    carry = 0
    
    while headA or headB or carry:
        val1 = headA.data if headA else 0
        val2 = headB.data if headB else 0
        curr.next = Node((val1 + val2 + carry)%10)
        carry = (val1 + val2 + carry)//10
        curr = curr.next
        headA = headA.next if headA else None
        headB = headB.next if headB else None

    return reverse(headC.next)
# T(n) = O(max(LL1, LL2))

ll1, ll2 = LL(), LL()
ll1.append(Node(1))
ll1.append(Node(2))
ll1.print()
ll2.append(Node(9))
ll2.print()

ll3 = sumOfLL(ll1.head, ll2.head)
while ll3:
    print(ll3.data, end=" -> ")
    ll3 = ll3.next
print()