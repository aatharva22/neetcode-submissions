class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        box = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                index = (i // 3)  + (j // 3 ) * 3 
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in box[index]:
                    return False
                else:
                    row[i][board[i][j]] = 0
                    col[j][board[i][j]] = 0
                    box[index][board[i][j]] = 0
        return True