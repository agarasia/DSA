def solveSudoku(board):
    def isValid(row, col, num):
        for i in range(9):
            if board[row][i] == num:
                return False
            if board[i][col] == num:
                return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3] == num:
                return False
        
        return True
            

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ".":
                for n in "123456789":
                    if isValid(i, j, n):
                        board[i][j] = n
                        if solveSudoku(board):
                            return True
                        return False
    
    return True

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

print(solveSudoku(board))