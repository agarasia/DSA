def dfs(v, adj):
    res = [0]
    visited = [False]*v
    visited[0] = True

    def dfsHelper(root):
        for edge in adj[root]:
            if not visited[edge]:
                res.append(edge)
                visited[edge] = True
                dfsHelper(edge)
    
    dfsHelper(0)
    return res

v = 5
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
print(dfs(v, adj))