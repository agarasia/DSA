from collections import deque

def isCycle(V, adj):
    visited = set()

    def hasCycle(vertex, parent):
        visited.add(vertex)

        for edge in adj[vertex]:
            if edge == parent:
                continue
            elif edge in visited:
                return True
            else:
                if hasCycle(edge, vertex):
                    return True
        
        return False
    
    for i in range(V):
        if i not in visited:
            if hasCycle(i, -1):
                return True
    
    return False
# T(n) = O(V + E)
# S(n) = O(V)


V = 5
adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
print(isCycle(V, adj))