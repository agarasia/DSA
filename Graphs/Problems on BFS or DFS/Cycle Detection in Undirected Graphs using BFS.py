from collections import deque

def isCycle(V, adj):
    visited = set()

    def hasCycle(vertex):
        queue = deque()
        queue.append([vertex, -1])

        while queue:
            node, parent = queue.popleft()

            for edge in adj[node]:
                if edge not in visited:
                    visited.add(edge)
                    queue.append([edge, node])
                elif edge != parent:
                    return True

        return True
    
    for i in range(V):
        if i not in visited:
            if hasCycle(i):
                return True
    
    return False
# T(n) = O(V + E)
# S(n) = O(V)


V = 5
adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
print(isCycle(V, adj))