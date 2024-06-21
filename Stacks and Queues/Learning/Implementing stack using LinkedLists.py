class StackNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class myStack:
    def __init__(self) -> None:
        self.head = None
    
    def push(self, data):
        if not self.head:
            self.head = StackNode(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = StackNode(data)

    def pop(self):
        if not self.head:
            return -1
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            res = curr.next
            curr.next = None
            return res.data
    
    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next


s = myStack()
print(s.pop())
s.push(1)
s.push(2)
s.print()
print()
print(s.pop())
s.print()