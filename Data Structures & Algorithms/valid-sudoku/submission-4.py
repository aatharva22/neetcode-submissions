class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        box = [{} for _ in range(9)]

        for i in range(9):

            for j in range(9):
                box_index = (i // 3) * 3 + (j // 3)
                if board[i][j] == ".":
                    continue
                
                elif board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in box[box_index]:
                    return False
                row[i][board[i][j]] = 1
                col[j][board[i][j]] = 1
                box[box_index][board[i][j]] = 1

        return True