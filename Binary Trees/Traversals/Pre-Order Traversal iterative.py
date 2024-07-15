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
def preOrderTraversal(root):
    res, stack = [], []
    stack.append(root)

    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
    return res
# T(n) = O(n)
# S(n) = O(n)

vec = [1,2,3,4,5]
root = Node(vec[0])
print(preOrderTraversal(createTree(root, vec)))