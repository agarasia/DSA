def solveMaze(maze):

    def solve(ans, r, c, temp):
        if r == len(maze) - 1 and c == len(maze) - 1:
            ans.append(temp)
            return
        
        if r+1 < len(maze) and maze[r+1][c] == 1:
            solve(ans, r+1, c, temp + 'D')
        if c+1 < len(maze) and maze[r][c+1] == 1:
            solve(ans, r, c+1, temp + 'R')

    ans = []
    temp = ""
    solve(ans, 0, 0, temp)
    return ans

maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]]
print(solveMaze(maze))
print(solveMaze([[1, 0], [1, 0]]))