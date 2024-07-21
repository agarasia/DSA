class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None

def createTree(vec : list[TreeNode]):
    root = vec[0]

    for i in range(len(vec)):
        c1, c2 = 2*i+1, 2*i+2
        if c1 < len(vec) and vec[c1].val != None:
            vec[i].left = vec[c1]
        if c2 < len(vec) and vec[c2].val != None:
            vec[i].right = vec[c2]
    
    return root

def search(root:TreeNode, key:int):
    def dfs(root):
        if not root:
            return None
        if root.val > key:
            return dfs(root.left)
        if root.val < key:
            return dfs(root.right)
        if root.val == key:
            return root
    
    return dfs(root)
# T(n) = O(n)
# S(n) = O(1)

vec = [TreeNode(9),
       TreeNode(None), TreeNode(10),
       TreeNode(None), TreeNode(None), TreeNode(None), TreeNode(11)]
print(search(createTree(vec), 11))