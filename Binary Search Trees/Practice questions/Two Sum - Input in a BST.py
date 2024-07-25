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

def twoSum(root, k):

    arr = []
    def inorder(root):
        if not root:    return
        inorder(root.left)
        arr.append(root.val)
        inorder(root.right)
    
    inorder(root)
    hashMap = {}

    for i in range(len(arr)):
        hashMap[arr[i]] = i
    
    for i in hashMap:
        if (k - i) in hashMap and hashMap[k - i] != hashMap[i]:
            return True
    
    return False
# T(n) = O(height of BST)
# S(n) = O(1)

vec = [TreeNode(5),
       TreeNode(3), TreeNode(6),
       TreeNode(2), TreeNode(4), TreeNode(None), TreeNode(7)]
print(twoSum(createTree(vec), k = 28))