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

    # Approach: take the linked list into a spare
    #           array and check if it(the array) is 
    #           palindrome or not.
    def palindromeBruteForce(self):
        lst = []
        curr = self.head
        while curr:
            lst.append(curr.data)
            curr = curr.next
        
        lstA = lst[::-1]
        return lst == lstA
    # T(n) = O(n)   
    # S(n) = O(n)

    # Approach: Reach halfway, and then compare each
    #           key in the linked list.
    def palindromeOptimal(self):
        def reverse(head):
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            return prev
        
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        halfway = reverse(slow)
        curr = self.head

        while curr != halfway and halfway:
            if curr.data != halfway.data:
                return False
        
            curr = curr.next
            halfway = halfway.next
        
        return True
# T(n) = O(n)

ll = LL()
ll.append(Node(1))
ll.append(Node(2))
ll.append(Node(2))
ll.append(Node(1))
ll.print()
print(ll.palindromeBruteForce())
print(ll.palindromeOptimal())