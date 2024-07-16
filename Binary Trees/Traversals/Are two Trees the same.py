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
def sameTree(p, q):
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
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level.append(None)
            if level:
                res.append(level)
        
        return res

    print(bfs(p) == bfs(q))
# T(n) = O(n)
# S(n) = O(n)

vec1 = [1, None, 2]
vec2 = [1, 2]
root1, root2 = Node(vec1[0]), Node(vec2[0])
createTree(root1, vec1), createTree(root2, vec2)
sameTree(root1, root2)