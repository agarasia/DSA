class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None

def buildTreeBruteForce(inorder:list[int], postorder:list[int]):
    if not inorder:
        return None
    
    root = TreeNode(postorder.pop())
    idx = inorder.index(root.val)

    root.right = buildTreeBruteForce(inorder[idx+1:], postorder)
    root.left = buildTreeBruteForce(inorder[:idx], postorder)

    return root
# T(n) = O(n ** 2)
# S(n) = O(1)

def buildTreeOptimal(inorder:list[int], postorder:list[int]):
    hashMap = {v: i for i, v in enumerate(inorder)}

    def helper(left, right):
        if left > right:
            return None
        
        root = TreeNode(postorder.pop())
        idx = hashMap[root.val]

        root.right = helper(idx+1, right)
        root.left = helper(left, idx-1)

        return root
    
    return helper(0, len(inorder)-1)
# T(n) = O(n)
# S(n) = O(n)


inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
buildTreeBruteForce(inorder, postorder)
postorder = [9,15,7,20,3]
buildTreeOptimal(inorder, postorder)