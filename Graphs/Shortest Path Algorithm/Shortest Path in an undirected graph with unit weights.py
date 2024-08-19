from collections import defaultdict, deque

def shortestPath(n, edges, src):
    ans = [-1] * n
    graph = defaultdict(list)
    for source, dest in edges:
        graph[source].append(dest)
        graph[dest].append(source)
    
    ans[src] = 0

    queue = deque([src])
    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if ans[nei] == -1:
                ans[nei] = ans[node] + 1
                queue.append(nei)

    return ans
        

n = 9
edges = [[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]]
src = 0
print(shortestPath(n, edges, src))