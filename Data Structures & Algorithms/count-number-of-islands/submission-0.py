class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == "1":
                    island += 1
                    self.dfs(grid,i,j)
                
        return island

    def dfs(self,grid,i,j):
            
        if  i == len(grid) or j == len(grid[0]) or i == -1 or j == -1 or grid[i][j] == "0":
                        return
        grid[i][j] = "0"

        self.dfs(grid,i+1, j)
        self.dfs(grid,i-1, j)
        self.dfs(grid,i, j+1)
        self.dfs(grid,i, j-1)

                
