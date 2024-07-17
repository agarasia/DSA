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
def bottomView(root):
    hashMap = {}
    
    def dfs(x, y, node):
        if not node:
            return
        
        dfs(x-1, y+1, node.left)
        dfs(x+1, y+1, node.right)
        
        if node.val != None:
            if (x, y) not in hashMap:
                hashMap[(x, y)] = []
            
            hashMap[(x, y)] += [node.val]
    
    dfs(0, 0, root)

    ans = []
    old = ['-inf', '-inf']
    for key, value in sorted(hashMap.items()):
        if key[0] != old[0]:
            if len(value) > 1:
                v = value[-1]
                ans.append(v)
            else:
                ans.append(value[0])
            old = key
        else:
            if len(value) > 1:
                v = value[-1]
                ans[-1] = v
            else:
                ans[-1] = value[0]
    
    return ans
# T(n) = O(n * log n)
# S(n) = O(n)

vec1 = [20, 8, 22, 5, 3, 4, 25, None, None, 10, None, None, 14, None, None]
root1= Node(vec1[0])
print(bottomView(createTree(root1, vec1)))