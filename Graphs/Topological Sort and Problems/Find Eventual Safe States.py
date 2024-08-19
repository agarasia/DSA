def eventualSafeNodes(graph):
    safe = {}
    ans = []

    def dfs(node):
        if node in safe:
            return safe[node]
        safe[node] = False
        for nei in graph[node]:
            if not dfs(nei):
                return safe[nei]
        safe[node] = True
        return safe[node]
    
    for i in range(len(graph)):
        if dfs(i):
            ans.append(i)
    return ans
# T(n) = O(V + E)
# S(n) = O(V)

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(eventualSafeNodes(graph))