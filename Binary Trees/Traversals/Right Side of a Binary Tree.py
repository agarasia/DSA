from collections import deque


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
    def bfs(root):
        queue = deque([root])
        res = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        
        return res
    
    res = bfs(root)
    
    ans = [row[-1] for row in res]
    return ans
# T(n) = O(n)
# S(n) = O(n)

vec1 = [1, 2]
root1= Node(vec1[0])
print(bottomView(createTree(root1, vec1)))