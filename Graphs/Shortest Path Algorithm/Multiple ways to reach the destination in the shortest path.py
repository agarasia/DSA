from heapq import heappop, heappush
from collections import defaultdict

def countPaths(n, roads):
    graph = defaultdict(list)
    for v1, v2, w in roads:
        graph[v1].append((v2, w))
        graph[v2].append((v1, w))
    
    dist, ways = [float('inf')] * n, [0] * n
    dist[0] = 0
    ways[0] = 1

    heap = [(0, 0)]     # dist, node
    mod = 10**9 + 7

    while heap:
        curr_dist, node = heappop(heap)
            
        if curr_dist > dist[node]:
            continue
        
        for nei, wei in graph[node]:
            new_dist = curr_dist + wei
            if new_dist < dist[nei]:
                dist[nei] = new_dist
                ways[nei] = ways[node]
                heappush(heap, (new_dist, nei))
            elif new_dist == dist[nei]:
                ways[nei] = (ways[nei] + ways[node]) % mod
    
    return ways[-1] % mod
# T(n) = O(V * log E)
# S(n) = O(V) + O(V)

n, roads = 7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(countPaths(n, roads))