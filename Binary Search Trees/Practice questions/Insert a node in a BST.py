class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None

def createTree(vec):
    root = vec[0]

    for i in range(len(vec)):
        c1, c2 = 2*i+1, 2*i+2
        if c1 < len(vec) and vec[c1].val != None:
            vec[i].left = vec[c1]
        if c2 < len(vec) and vec[c2].val != None:
            vec[i].right = vec[c2]
    
    return root

def insert(root, k):
    curr = root
    while True:
        if k > curr.val:
            if not curr.right:
                curr.right = TreeNode(k)
                return root
            curr = curr.right
        if k < curr.val:
            if not curr.left:
                curr.left = TreeNode(k)
                return root
            curr = curr.left
# T(n) = O(height of BST)
# S(n) = O(height of BST)

vec = [TreeNode(40),
       TreeNode(20), TreeNode(60),
       TreeNode(10), TreeNode(30), TreeNode(50), TreeNode(70)]
print(insert(createTree(vec), 25))