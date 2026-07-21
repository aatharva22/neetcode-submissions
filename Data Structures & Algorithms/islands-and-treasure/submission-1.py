class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        queue = deque()

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 0:
                    queue.append((i,j))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:

            i,j = queue.popleft()

            for dr,dc in directions:
                nr,nc = i+dr, j+dc

                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == 2147483647:


                    grid[nr][nc] = grid[i][j] + 1
                    queue.append((nr,nc))
        
