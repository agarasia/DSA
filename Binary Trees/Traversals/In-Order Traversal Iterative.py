class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = 0

def createTree(root, vec):
    aux = [root]
    
    for i in range(1, len(vec)):
        aux.append(Node(vec[i]))
    
    for i in range(len(vec)):
        c1, c2 = 2*i+1, 2*i+2
        if c1 < len(vec):
            aux[i].left = aux[c1]
        if c2 < len(vec):
            aux[i].right = aux[c2]
    
    return root

# Main program
def inOrderTraversal(root):
    # Initialize an empty list to store the result (in-order traversal)
    res = []
    
    # Initialize an empty stack for iterative traversal
    stack = []
    
    # Loop until either the current node is not None or the stack is not empty
    while root or stack:
        # Traverse to the leftmost node and push each encountered node onto the stack
        while root:
            stack.append(root)
            root = root.left

        # Pop the last node from the stack (most recently left-visited node)
        root = stack.pop()
        
        # Append the value of the popped node to the result list
        res.append(root.val)
        
        # Move to the right subtree to continue the in-order traversal
        root = root.right
    
    # Return the final result list
    return res
# T(n) = O(n)
# S(n) = O(n)

vec = [1, None, 2, 3]
root = Node(vec[0])
print(createTree(root, vec))