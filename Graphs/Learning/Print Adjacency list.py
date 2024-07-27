from collections import defaultdict


def printGraph(v, edges):
    hashMap = defaultdict(list[int])
    res = []

    for edge in edges:
        hashMap[edge[0]].append(edge[1])
        hashMap[edge[1]].append(edge[0])
    
    for vertex in range(v):
        hashMap[vertex].sort()
        res.append(hashMap[vertex])

    return res
# T(n) = O(V + E)
# S(n) = O(V + E)

v = 5
edges = [[0, 1], [0, 4], [4, 1], [4, 3], [1, 3], [1, 2], [3, 2]]
print(printGraph(v, edges))
    