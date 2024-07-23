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

def kthSmallest(root, k):
    stack = []
    curr = root
    n = 0

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        n += 1
        if n == k:
            return curr.val
        curr = curr.right
# T(n) = O(height of BST)
# S(n) = O(height of BST)

vec = [TreeNode(3),
       TreeNode(1), TreeNode(4),
       TreeNode(None), TreeNode(2), TreeNode(None), TreeNode(None)]
print(kthSmallest(createTree(vec), 1))