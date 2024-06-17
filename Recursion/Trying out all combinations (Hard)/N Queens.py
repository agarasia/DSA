def nQueens(n):

    def isSafe(row, col, board):
        dupRow, dupCol = row, col

        # checking upper diagonal
        while dupRow >= 0 and dupCol >= 0:
            if board[dupRow][dupCol] == 'Q':
                return False
            dupRow -= 1
            dupCol -= 1

        dupRow, dupCol = row, col

        # checking same row:
        while dupCol >= 0:
            if board[dupRow][dupCol] == 'Q':
                return False
            dupCol -= 1
        
        dupRow, dupCol = row, col

        # checking lower diagonal
        while dupRow < n and dupCol >= 0:
            if board[dupRow][dupCol] == 'Q':
                return False
            dupRow += 1 
            dupCol -= 1

        return True
    

    def solve(board, col, ans):
        if col == n:
            ans.append(list(board))
            return
        
        for i in range(n):
            if isSafe(i, col, board):
                board[i] = board[i][:col] + 'Q' + board[i][col+1:]
                solve(board, col + 1, ans)
                board[i] = board[i][:col] + '.' + board[i][col+1:]

    ans = []
    board = ['.'*n for _ in range(n)]
    solve(board, 0, ans)
    return ans

queens = 4
print(nQueens(queens))