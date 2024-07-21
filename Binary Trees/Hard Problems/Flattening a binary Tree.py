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

def flatten(root):
    def dfs(root):
        if not root:
            return None
        
        leftTail = dfs(root.left)
        rightTail = dfs(root.right)

        if leftTail:
            leftTail.right = root.right
            root.right = root.left
            root.left = None
        
        last = rightTail or leftTail or root
        return last
    dfs(root)
# T(n) = O(n)
# S(n) = O(n)

vec = [Node(1),
       Node(2), Node(5),
       Node(3), Node(4), Node(None), Node(6)]
flatten(createTree(vec))