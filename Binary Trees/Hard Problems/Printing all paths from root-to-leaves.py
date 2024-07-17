class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None
    
def createTree(root:Node, vec:list):
    aux = [root]
    for i in range(1, len(vec)):
        aux.append(Node(vec[i]))

    for i in range(len(aux)):
        c1 = 2*i+1
        c2 = 2*i+2
        if c1 < len(vec):
            if aux[c1].val != None:
                aux[i].left = (aux[c1])
        if c2 < len(vec):
            if aux[c2].val != None:
                aux[i].right = (aux[c2])
    
    return root

def allPaths(root):
    def helper(node, temp, ans):
        if not node:
            return
        
        temp.append(node.val)

        if not node.left and not node.right:
            ans.append(temp[:])
            del temp[-1]
            return
        
        helper(node.left, temp, ans)
        helper(node.right, temp, ans)
        del temp[-1]
    
    ans = []
    helper(root, [], ans)

    return ans
# T(n) = O(n)
# S(n) = O(n)

root = Node(1)
vec = [1, 2, 4, 3]
print(allPaths(createTree(root, vec)))
