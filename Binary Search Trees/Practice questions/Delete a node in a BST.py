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

def delete(root, k):
    if not root:
        return root
    
    if k > root.val:
        root.right = delete(root.right, k)
    elif k < root.val:
        root.left = delete(root.left, k)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        curr = root.right
        while curr.left:
            curr = curr.left
        root.val = curr.val
        root.right = delete(root.right, root.val)
    
    return root
# T(n) = O(height of BST)
# S(n) = O(height of BST)

vec = [TreeNode(5),
       TreeNode(3), TreeNode(6),
       TreeNode(2), TreeNode(4), TreeNode(None), TreeNode(7)]
print(delete(createTree(vec), 3))