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
def diameterOfBinaryTrees(root):
    def dfs(node):
        if not node:
            return 0, 0  # (max depth, max diameter)

        left_depth, left_diameter = dfs(node.left)
        right_depth, right_diameter = dfs(node.right)

        max_depth = 1 + max(left_depth, right_depth)
        diameter_through_root = left_depth + right_depth
        max_diameter = max(diameter_through_root, left_diameter, right_diameter)

        return max_depth, max_diameter

    _, diameter = dfs(root)
    return diameter
# T(n) = O(n)
# S(n) = O(n)

vec = [1, None, 2, 3]
root = Node(vec[0])
print(diameterOfBinaryTrees(createTree(root, vec)))