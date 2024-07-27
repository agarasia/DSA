from collections import deque


def bfs(V, adj):
    queue = deque([0])
    res = []
    visited = [0]*V

    visited[0] = 1

    while queue:
        v = queue.popleft()
        res.append(v)
        for edge in adj[v]:
            if visited[edge] != 1:
                queue.append(edge)
                visited[v] = 1
    
    return res

v = 5
adj = [[1, 2, 3], [], [4], [], []]
print(bfs(v, adj))