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

def ceil(root, k):
    res = []
    def dfs(root):
        if not root:
            return
        if root.val >= k:
            res.append(root.val)
            dfs(root.left)
        if root.val < k:
            dfs(root.right)
    
    dfs(root)
    return res[-1] if res else -1
# T(n) = O(height of BST)
# S(n) = O(height of BST)

vec = [TreeNode(5),
       TreeNode(1), TreeNode(7),
       TreeNode(None), TreeNode(3), TreeNode(None), TreeNode(None)]
print(ceil(createTree(vec), 8))