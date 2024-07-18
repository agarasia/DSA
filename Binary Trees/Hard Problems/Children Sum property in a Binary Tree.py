from collections import deque

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None
    
def createTree(root:Node, vec:list):
    aux = [root]
    for i in range(1, len(vec)):
        aux.append(Node(vec[i]))

    for i in range(len(aux)):
        c1 = 2*i+1
        c2 = 2*i+2
        if c1 < len(vec):
            if aux[c1].val != None:
                aux[i].left = (aux[c1])
        if c2 < len(vec):
            if aux[c2].val != None:
                aux[i].right = (aux[c2])
    
    return root

# Main Program
def isSumProperty(root:Node):
    def getVal(node:Node):
        return node.val if node else 0
    
    def dfs(node:Node):
        if not node or (not node.left and not node.right):
            return True
        
        left = dfs(node.left)
        right = dfs(node.right)

        if node.left or node.right:
            return left and right and (getVal(node) == getVal(node.left) + getVal(node.right))
        
        return left and right
    
    return dfs(root)
# T(n) = O(n)
# S(n) = O(log n)

root = Node(35)
vec = [35, 20, 15, 15, 5, 10, 5]
print(isSumProperty(createTree(root, vec)))
