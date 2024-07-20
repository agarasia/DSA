from collections import defaultdict, deque


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None

def createTree(vec):
    root = vec[0]

    for i in range(len(vec)):
        c1, c2 = 2*i+1, 2*i+2
        if c1 < len(vec):
            vec[i].left = vec[c1]
        if c2 < len(vec):
            vec[i].right = vec[c2]
    
    return root

def numberOfNodesBruteForce(root):
    if not root:
        return 0
    
    queue = deque([root])
    ans = 0

    while queue:
        node = queue.popleft()
        if node.left:
            ans += 1
            queue.append(node.left)
        if node.right:
            ans += 1
            queue.append(node.right)
    
    return ans
# T(n) = O(n)
# S(n) = O(n)

def numberOfNodesOptimal(root):
    def findLeftHeight(node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
    
    def findRightHeight(node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height
    
    if not root:
        return 0
    
    leftHeight = findLeftHeight(root)
    rightHeight = findRightHeight(root)

    if leftHeight == rightHeight:
        return (1 << leftHeight) - 1
    return 1 + numberOfNodesOptimal(root.left) + numberOfNodesOptimal(root.right)


vec = [Node(1),
       Node(2), Node(3),
       Node(4), Node(5), Node(None), Node(6)]

print(numberOfNodesBruteForce(createTree(vec)))
print(numberOfNodesOptimal(createTree(vec)))