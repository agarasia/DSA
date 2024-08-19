import heapq

def djikstra(V, adj, src):
    dist = [float('inf')] * V
    dist[src] = 0

    heap = [(0, src)]
    while heap:
        curr, node = heapq.heappop(heap)

        if curr > dist[node]:
            continue

        for nei, wei in adj[node]:
            if dist[node] + wei < dist[nei]:
                dist[nei] = dist[node] + wei
                heapq.heappush(heap, (dist[node] + wei, nei))
    
    for i in range(V):
        if dist[i] == float('inf'):
            dist[i] = -1
    
    return dist
# T(n) = O(V + E)
# S(n) = O(V)

adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
V = 3
src = 2
print(djikstra(V, adj, src))