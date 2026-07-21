class Solution:
    def solve(self, board):
        rows, cols = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(i, j):
            if (i < 0 or i >= rows or 
                j < 0 or j >= cols or 
                board[i][j] != 'O'):
                return
            
            board[i][j] = '!'
            for dr, dc in directions:
                dfs(i + dr, j + dc)
        
        # Mark all border-connected 'O's as safe
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == 'O':
                    dfs(r, c)
        
        # Flip: '!' → 'O' (safe), 'O' → 'X' (surrounded)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '!':
                    board[r][c] = 'O'