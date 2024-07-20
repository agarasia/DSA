class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None

def createTree(preorder:list[int], inorder:list[int]):
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    ind = inorder.index(preorder[0])
    root.left = createTree(preorder[1 : ind + 1], inorder[: ind + 1])
    root.right = createTree(preorder[ind + 1 : ], inorder[ind + 1 : ])

    return root
# T(n) = O(n)
# S(n) = O(1) if not considering recursive stack else O(n)

inorder = [9,3,15,20,7]
preorder = [3,9,20,15,7]
print(createTree(preorder, inorder))