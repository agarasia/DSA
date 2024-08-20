from collections import deque

def shortestPath(grid):
    n = len(grid)
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1

    visited = set((0, 0))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    queue = deque([(1, 0, 0)])
    while queue:
        dist, x ,y = queue.popleft()
        if (x, y) == (n-1, n-1):
            return dist
        
        for dx, dy in directions:
            i = x + dx
            j = y + dy
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 0 and (i, j) not in visited:
                visited.add((i, j))
                queue.append((dist + 1, i, j))
    return -1

grid = [[0,0,0],[1,1,0],[1,1,0]]
print(shortestPath(grid))
