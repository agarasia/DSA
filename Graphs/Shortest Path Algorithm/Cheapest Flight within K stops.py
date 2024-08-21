import heapq
from collections import defaultdict

def findCheapestPrice(flights, src, dst, k):
    n = len(flights)
    adj = [[] for i in range(n)]
    for i, j, l in flights:
        adj[i].append([j, l])

    dis = [float("inf") for _ in range(n)]
    dis[src] = 0
    heap = [(0, 0, src)]
    while heap:
        stops, price, city = heapq.heappop(heap)
        for c in adj[city]:
            if c[0] == dst:
                if stops <= k and (price + c[1]) < dis[dst]:
                    dis[dst] = price + c[1]
            else:
                if stops < k and (price + c[1]) < dis[c[0]]:
                    dis[c[0]] = price + c[1]
                    heapq.heappush(heap, (stops + 1, price + c[1], c[0]))
    if dis[dst] == float("inf"):
        return -1
    return dis[dst]
# T(n) = O(V + E)
# S(n) = O(V)

flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src, dst, k = 0, 3, 1
print(findCheapestPrice(flights, src, dst, k))