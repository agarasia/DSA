from collections import defaultdict
import heapq

def shortestPaths(n, edges):
    ans = [float('inf')] * n
    ans[0] = 0
    graph = defaultdict(list)

    for v1, v2, w in edges:
        graph[v1].append([v2, w])
    
    heap = [(0, 0)]
    while heap:
        currDist, node = heapq.heappop(heap)
        if currDist > ans[node]:
            continue

        for nei, wei in graph[node]:
            ans[nei] = wei + currDist
            heapq.heappush(heap, (wei + currDist, nei))
    
    return ans
# T(n) = O(V + E)
# S(n) = O(V)

n, edges = 6, [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
print(shortestPaths(n, edges))