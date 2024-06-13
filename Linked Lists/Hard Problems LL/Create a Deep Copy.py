class Node:
    def __init__(self, data) -> None:
        self.val = data
        self.next = None
        self.random = None

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
            print(curr.val, end= " -> ")
            curr = curr.next
        print()

    def insertCopyInBetween(head):
        temp = head
        while temp:
            nextElement = temp.next

            copy = Node(temp.val)
            copy.next = nextElement

            temp.next = copy
            temp = nextElement
    
    def connectRandomPointers(head):
        temp = head
        while temp:
            # Access the copied node
            copyNode = temp.next

            # If the original node
            # has a random pointer
            if temp.random:
                # Point the copied node's random to the
                # corresponding copied random node
                copyNode.random = temp.random.next
            else:
                # Set the copied node's random to
                # null if the original random is null
                copyNode.random = None

            # Move to the next original node
            temp = temp.next.next
    
    def getDeepCopyList(head):
        temp = head
        # Create a dummy node
        dummyNode = Node(-1)
        # Initialize a result pointer
        res = dummyNode

        while temp:
            # Creating a new List by
            # pointing to copied nodes
            res.next = temp.next
            res = res.next

            # Disconnect and revert back to the
            # initial state of the original linked list
            temp.next = temp.next.next
            temp = temp.next

        # Return the deep copy of the
        # list starting from the dummy node
        return dummyNode.next

# Function to clone the linked list
    def cloneLL(self):
        # If the original list
        # is empty, return null
        if not self.head:
            return None

        # Step 1: Insert copy of
        # nodes in between
        self.insertCopyInBetween(self.head)
        # Step 2: Connect random
        # pointers of copied nodes
        self.connectRandomPointers(self.head)
        # Step 3: Retrieve the deep
        # copy of the linked list
        return self.getDeepCopyList(self.head)
