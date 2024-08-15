def topoSort(adj):
    visited = [0] * len(adj)
    st = []

    def dfs(node):
        visited[node] = 1
        for edge in adj[node]:
            if not visited[edge]:
                dfs(edge)
        st.append(node)
    
    for i in range(len(adj)):
        if not visited[i]:
            dfs(i)
    
    ans = []
    while st:
        ans.append(st.pop())
    
    return ans
# T(n) = O(V + E)
# S(n) = O(V)

adj = [[], [0], [0], [0]]
print(topoSort(adj))