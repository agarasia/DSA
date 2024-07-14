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


vec = [1,2,3,4,5,6,7]
root = Node(vec[0])
root = createTree(root, vec)