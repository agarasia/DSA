from collections import deque


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
# T(n) = O(n)
# S(n) = O(n)

# Main program
def isSymmetric(root):
    def helper(node1, node2):
        if not node1 or not node2:
            return node1 == node2
        return (node1.val == node2.val and
                helper(node1.left, node2.right) and
                helper(node1.right, node2.left))
    
    if not root:
        return True
    return helper(root.left, root.right)
# T(n) = O(n)
# S(n) = O(1)

vec1 = [1, 2]
root1= Node(vec1[0])
print(isSymmetric(createTree(root1, vec1)))