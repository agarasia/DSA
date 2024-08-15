from collections import deque

def topoSortKahn(adj):
    indegree = [0] * len(adj)

    for i in range(len(adj)):
        for edge in adj[i]:
            indegree[edge] += 1
    
    q = deque()
    for i in range(len(adj)):
        if indegree[i] == 0:
            q.append(i)
    
    ans = []
    while q:
        node = q.popleft()
        ans.append(node)

        for i in adj[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    return ans
# T(n) = O(V + E)
# S(n) = O(V)

adj = [[], [0], [0], [0]]
print(topoSortKahn(adj))