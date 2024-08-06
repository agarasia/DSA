from collections import deque

def updateMatrix(mat):
    m, n = len(mat), len(mat[0])
    dist = [[float('inf')] * n for _ in range(m)]
    queue = deque()

    # Initialize the queue with all 0s
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                queue.append((i, j))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # BFS to find the shortest distance to 0
    while queue:
        i, j = queue.popleft()
        for di, dj in directions:
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < m and 0 <= new_j < n:
                if dist[new_i][new_j] > dist[i][j] + 1:
                    dist[new_i][new_j] = dist[i][j] + 1
                    queue.append((new_i, new_j))

    return dist
# T(n) = O(m * n)
# S(n) = O(m * n)

mat = [[0, 0, 0],
       [0, 1, 0],
       [1, 1, 1]]
print(updateMatrix(mat))