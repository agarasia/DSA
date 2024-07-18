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
def maxWidth(root):
    res = 0
    queue = deque([[root, 1, 1]])   # [node, level, num]
    prevLevel, prevNum = 1, 1

    while queue:
        node, level, num = queue.popleft()

        if level > prevLevel:
            prevLevel = level
            prevNum = num
        
        if node.left:
            queue.append([node.left, level + 1, 2*num])
        if node.right:
            queue.append([node.right, level + 1, 2*num + 1])
        
        res = max(res, num - prevNum + 1)
    
    return res
    
# T(n) = O(n)
# S(n) = O(n)

root = Node(1)
vec = [1, 3, 2, 5, 3, None, 9]
print(maxWidth(createTree(root, vec)))
