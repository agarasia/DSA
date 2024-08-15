from collections import deque

def isCyclic(adj):
    indegree = [0] * len(adj)
    for i in range(len(adj)):
        for e in adj[i]:
            indegree[e] += 1
    
    q = deque()
    processedNodes = 0
    for i in range(len(adj)):
        if indegree[i] == 0: 
            q.append(i)
    
    while q:
        node = q.popleft()
        processedNodes += 1

        for i in adj[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    if processedNodes != len(adj):
        return True
    else:
        return False
# T(n) = O(V + E)
# S(n) = O(V)

adj = [[1],[2],[3],[3]]
print(isCyclic(adj))