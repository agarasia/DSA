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
def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root

    l = lowestCommonAncestor(root.left, p, q)
    r = lowestCommonAncestor(root.right, p, q)

    if l and r:
        return root
    return l if l else r
    
# T(n) = O(n)
# S(n) = O(n)

root = Node(1)
vec = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None]
print(lowestCommonAncestor(createTree(root, vec), Node(5), Node(2)))
