class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None

def createTree(pre):
    idx = 0
    def helper(lower = float('-inf'), upper = float('inf')):
        nonlocal idx
        if idx == len(pre):
            return None
        
        val = pre[idx]
        if val > upper or val < lower:
            return None
        
        idx += 1
        root = TreeNode(val)
        root.left = helper(lower, val)
        root.right = helper(val, upper)
        
        return root
    
    return helper()
# T(n) = O(n)
# S(n) = O(n)

preorder = [8, 5, 1, 7, 10, 12]
createTree(preorder)