from collections import deque


def timeToRot(grid):
    queue = deque()
    time, fresh = 0, 0
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                fresh += 1
            if grid[i][j] == 2:
                queue.append([i, j])

    while queue and fresh:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if ((row < 0 or row == len(grid)) or 
                (col < 0 or col == len(grid[0])) or 
                grid[row][col] != 1):
                    continue
                grid[row][col] = 2
                queue.append([row, col])
                fresh -= 1
        time += 1
    
    return time if fresh == 0 else -1
# T(n) = O(m * n)
# S(n) = O(m * n)

grid = [[2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]]
print(timeToRot(grid))