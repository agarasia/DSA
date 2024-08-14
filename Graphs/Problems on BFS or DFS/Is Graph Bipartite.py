from collections import deque

def isBipartite(graph):
    odd = [0] * len(graph)

    def bfs(i):
        if odd[i]:
            return True
        
        q = deque([i])
        odd[i] = -1
        while q:
            i = q.popleft()
            for nei in graph[i]:
                if odd[i] == odd[nei]:
                    return False
                elif not odd[nei]:
                    q.append(nei)
                    odd[nei] = -1 * odd[i]
        return True

    for v in range(len(graph)):
        if not bfs(v):
            return False
    return True

graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
print(isBipartite(graph))