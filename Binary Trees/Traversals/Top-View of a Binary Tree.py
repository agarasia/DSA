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
# T(n) = O(n)
# S(n) = O(n)

# Main program
def topView(root):
    hashMap = {}
    
    def dfs(x, y, node):
        if not node:
            return
        
        dfs(x-1, y+1, node.left)
        dfs(x+1, y+1, node.right)
        
        if (x, y) not in hashMap:
            hashMap[(x, y)] = []
        hashMap[(x, y)] += [node.val]
    
    dfs(0, 0, root)
    prev = '-inf'
    ans = []
    for key, value in sorted(hashMap.items()):
        if key[0] != prev:
            val = value[0]
            ans.append(val)
            prev = key[0]
    
    return ans
# T(n) = O(n * log n)
# S(n) = O(n)

vec1 = [1, 3, 2]
root1= Node(vec1[0])
print(topView(createTree(root1, vec1)))