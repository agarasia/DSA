def numberOfEnclaves(grid):
    R, C = len(grid), len(grid[0])

    def capture(r, c):
        if (r < 0 or r == R
            or c < 0 or c == C or
            grid[r][c] != 1):
            return
        
        grid[r][c] = -1
        capture(r + 1, c)
        capture(r - 1, c)
        capture(r, c - 1)
        capture(r, c + 1)
    
    # Getting all the unsurrounded regions
    for i in range(R):
        for j in range(C):
            if (grid[i][j] == 1 and 
                (i in [0, R - 1] or j in [0, C - 1])):
                capture(i, j)

    ans = 0
    # Capturing the surrounded regions
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                ans += 1
    
    return ans
# T(n) = O(n * m)
# S(n) = O(1)

grid = [[0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]]
print(numberOfEnclaves(grid))