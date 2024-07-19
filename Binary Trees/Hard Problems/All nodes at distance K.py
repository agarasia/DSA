from collections import deque, defaultdict

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

# Main Program
def kDistance(root:Node, target:Node, k:int):
    queue = deque([root])
    graph = defaultdict(list)

    while queue:
        node = queue.popleft()
        if node.left:
            graph[node].append(node.left)
            graph[node.left].append(node.right)
            queue.append(node.left)

        if node.right:
            graph[node].append(node.right)
            graph[node.right].append(node.right)
            queue.append(node.right)
    
    res = []
    visited = set([target])
    queue = deque([(target, 0)])

    while queue:
        node, distance = queue.popleft()

        if distance == k:
            res.append(node.val)
        else:
            for edge in graph[node]:
                if edge not in visited:
                    visited.add(edge)
                    queue.append((edge, distance + 1))
    
    return res
# T(n) = O(n)
# S(n) = O(n)

root = Node(3)
vec = [3,5,1,6,2,0,8,None,None,7,4]
print(kDistance(createTree(root, vec), Node(5), 4))
