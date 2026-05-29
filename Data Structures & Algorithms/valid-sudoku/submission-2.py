class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = {}
        col = {}
        box = {}

        for i in range(9):
            row[i] = {}
            col[i] = {}
            box[i] = {}
        
        for i in range(9):
            
            for j in range(9):
                if board[i][j] == ".":
                    continue
                #Box index
                k = ((j//3) * 3 ) + i // 3
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in box[k]:

                    return False
                else:
                    box[k][board[i][j]] = 1
                    row[i][board[i][j]] = 1
                    col[j][board[i][j]] = 1
            
        return True

                