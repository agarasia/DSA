class StackNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class myQueue:
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
            self.head = curr.next if curr.next else None
            return curr.data

    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next


q = myQueue()
print(q.pop())
q.push(1)
print(q.pop())
print(q.pop())
q.push(1)
q.push(2)
q.push(3)
q.print()