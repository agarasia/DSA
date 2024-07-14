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
def preOrderTraversal(root):
    def traversor(node, ans):
        if not node:
            return
        
        if node.val != -1:
            ans.append(node.val)
        traversor(node.left, ans)
        traversor(node.right, ans)
    
    ans = []
    traversor(root, ans)
    return ans
# T(n) = O(n)
# S(n) = O(n)

vec = [1,2,3,4,5]
root = Node(vec[0])
print(preOrderTraversal(createTree(root, vec)))