class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        #start on edges and dfs on O if found on edge, hange it to @ for sometime
        #then convert all @ to O and all remaining O to X

        directions = [(-1,0), (1,0), (0,-1), (0,1)] 
        def dfs(r,c):

            if 0<=r<len(board) and 0<=c<len(board[0]):

                for dr,dc in directions:

                    nr,nc = r-dr, c-dc

                    if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] == 'O':
                        board[nr][nc] = '!'
                        dfs(nr,nc)
        
        for col in range(len(board[0])):

            if board[0][col] == 'O' :
                board[0][col] = '!'
                dfs(0,col)
                
            if board[len(board) - 1][col] == 'O':
                board[len(board) - 1][col] = '!'
                dfs(len(board) - 1, col)
                
        
        for row in range(len(board)):

            if board[row][0] == 'O' :
                board[row][0] = '!'
                dfs(row,0)
            if board[row][len(board[0]) - 1] == 'O':
                board[row][len(board[0]) - 1] = '!'
                dfs(row, len(board[0]) - 1)
        
        for i in range(len(board)):

            for j in range(len(board[0])):

                if board[i][j] == '!':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
            

        

            
