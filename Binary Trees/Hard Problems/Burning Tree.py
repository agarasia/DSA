from collections import defaultdict, deque


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None

def createTree(vec):
    root = vec[0]

    for i in range(len(vec)):
        c1, c2 = 2*i+1, 2*i+2
        if c1 < len(vec):
            vec[i].left = vec[c1]
        if c2 < len(vec):
            vec[i].right = vec[c2]
    
    return root

def burningTree(root, target):
    graph = defaultdict(list)
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.left and node.left.val != None:
            graph[node].append(node.left)
            graph[node.left].append(node)
            queue.append(node.left)

        if node.right and node.right != None:
            graph[node].append(node.right)
            graph[node.right].append(node)
            queue.append(node.right)
    
    queue = deque([(target, 0)])
    visited = set([target])
    max_time = 0

    while queue:
        node, time = queue.popleft()
        max_time = max(max_time, time)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, time + 1))

    return max_time
# T(n) = O(n)
# S(n) = O(n)

vec = [Node(1),
       Node(2), Node(3),
       Node(4), Node(5), Node(None), Node(6),
       Node(None), Node(None), Node(7), Node(8), Node(None), Node(None), Node(None), Node(9),
       Node(None), Node(None),Node(None), Node(None),Node(None), Node(None),Node(None), Node(None),
       Node(None), Node(None),Node(None), Node(None),Node(None), Node(None),Node(None), Node(10),]

print(burningTree(createTree(vec), vec[10]))