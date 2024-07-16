class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = 0

def createTree(root, vec):
    aux = [root]
    
    for i in range(1, len(vec)):
        aux.append(Node(vec[i]))
    
    for i in range(len(vec)):
        c1, c2 = 2*i+1, 2*i+2
        if c1 < len(vec):
            aux[i].left = aux[c1]
        if c2 < len(vec):
            aux[i].right = aux[c2]
    
    return root

# Main program
def maxDepthSum(root):
    res = [root.val]

    def dfs(node):
        if not node:
            return 0
        
        leftSum = dfs(node.left)
        rightSum = dfs(node.right)
        # keeping the max value in case there's a negative val
        leftSum = max(leftSum, 0)
        rightSum = max(rightSum, 0)

        # SPLIT
        res[0] = max(res[0], node.val + leftSum + rightSum)

        # NOT SPLIT
        return node.val + max(leftSum, rightSum)
    
    dfs(root)
    return res[0]
# T(n) = O(n)
# S(n) = O(log n)

vec = [1, None, 2, 3]
root = Node(vec[0])
print(maxDepthSum(createTree(root, vec)))