class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        maxArea = 0

        for i in range(row):
            for j in range(col):

                if grid[i][j] == 1:
                    
                    maxArea = max(maxArea,self.dfs(grid,i,j))
        return maxArea
        
    def dfs(self,grid,i,j):

        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] == 0:
            return 0
        
        grid[i][j] = 0

        return (1 + self.dfs(grid,i+1,j)+self.dfs(grid,i-1,j)+self.dfs(grid,i,j+1)+self.dfs(grid,i,j-1))



