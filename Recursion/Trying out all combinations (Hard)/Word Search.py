def exists(board, word):
    def found(i, j, ind):
        # If word is found, return True
        if ind == len(word):
            return True
        
        # If out of box or not matching 
        # character, return False
        if( i < 0 or i >= len(board) or j < 0 or 
           j >= len(board[0]) or board[i][j] != word[ind]):
            return False
        
        temp = board[i][j]
        board[i][j] = ''

        # If found at adjacent places, return True
        if (found(i-1, j, ind+1) or found(i+1, j, ind+1) or
            found(i, j-1, ind+1) or found(i, j+1, ind+1)):
            return True
        
        board[i][j] = temp

        return False


    for i in range(len(board)):
        for j in range(len(board[0])):
            if found(i, j, 0):
                return True
    
    return False

grid = [["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]]
word = "ABCCED"

print(exists(grid, word))