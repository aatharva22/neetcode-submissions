class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.dfs(grid,i,j))
                
        return maxArea if maxArea > 0 else 0
    
    def dfs(self,grid,i,j) -> int:

        if i > len(grid) - 1 or i < 0 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] == 0:
            return 0
        
        grid[i][j] = 0

        return 1 + self.dfs(grid,i+1, j) + self.dfs(grid,i-1, j) + self.dfs(grid,i, j+1) + self.dfs(grid,i, j-1)