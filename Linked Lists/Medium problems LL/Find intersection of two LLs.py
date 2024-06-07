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

# Approach: Use a hash table to keep track of
#           which nodes have already been covered
def intersectionNodeBruteForce(headA, headB):
    hashTable = set()
    curr = headA
    
    while curr:
        hashTable.add(curr)
        curr = curr.next
    
    curr = headB

    while curr:
        if curr in hashTable:
            return curr
        curr = curr.next
    
    return None
# T(n) = O(n + m)
# S(n) = O(n + m)

# Approach: Keep traversing LLs until you intersect
#           at a common node. Assume that input LLs 
#           always have an intersection point, otw this
#           approach will fail.
def intersectionNodeOptimal(headA, headB):
    if not headA or not headB:
            return None
        
    currA, currB = headA, headB

    while currA != currB:
        currA = headB if not currA else currA.next
        currB = headA if not currB else currB.next

    return currA
# T(n) = O(n + m)
# S(n) = O(1)

ll1 = LL()
ll1.append(Node(1))
ll1.append(Node(3))
n1 = Node(1)
ll2 = LL()
ll2.append(Node(2))
ll2.append(Node(4))
n1.next = ll2.head
ll1.append(n1)
ll3 = LL()
n2 = Node(3)
n2.next = ll2.head
ll3.append(n2)

ll1.print()
ll3.print()


n4 = intersectionNodeBruteForce(ll1.head, ll3.head)
while n4:
    print(n4.data, end=" -> ")
    n4 = n4.next