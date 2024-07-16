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
def boundaryTraversal(root):
    def bfs(root):
        if not root:
            return []
        
        res, queue = [], []

        queue.append(root)

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    if node.val != -1:
                        level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res
        
    if not root:
        return []

    res = bfs(root)
    ans = []

    for i in range(len(res)-1):
        ans.append(res[i][0])
    
    for i in range(len(res[-1])):
        ans.append(res[-1][i])

    for i in range(len(res)-2, 0, -1):
        ans.append(res[i][-1])

    return ans
    
# T(n) = O(n)
# S(n) = O(n)

vec1 = [1, 2, 7, 3, -1, -1, 8, -1, 4, -1, -1, -1, -1, 9, -1]
root1= Node(vec1[0])
print(boundaryTraversal(createTree(root1, vec1)))
