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
def zigZag(root):
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
                    if node.val != None:
                        level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res
        
    if not root:
        return []

    res = bfs(root)
    for i in range(len(res)):
        if i%2:
            res[i].reverse()
    
    return res
# T(n) = O(n)
# S(n) = O(log n)

vec1 = [3,9,20,None,None,15,7]
root1= Node(vec1[0])
print(zigZag(createTree(root1, vec1)))
