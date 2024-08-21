import heapq
from collections import defaultdict

def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for p1, p2, w in times:
        graph[p1].append([p2, w])
    
    dist = [float('inf')] * (n + 1)
    dist[0] = float('-inf')
    dist[k] = 0
    heap = [(0, k)]
    
    while heap:
        dis, p1 = heapq.heappop(heap)
        if dis > dist[p1]:
            continue
        for p2, w in graph[p1]:
            if w + dis < dist[p2]:
                dist[p2] = w + dis
                heapq.heappush(heap, (w + dis, p2))
    
    return max(dist) if max(dist) != float('inf') else -1


times = [[1,2,1], [2,1,3]]
n, k = 2, 2
print(networkDelayTime(times, n, k))