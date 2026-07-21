class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh = 0
        queue = deque()
        minutes = 0

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    fresh += 1
                if  grid[i][j] == 2:
                    queue.append((i,j))
        
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue and fresh > 0 :
            
            for _ in range(len(queue)):
                

                i,j = queue.popleft()

                for dr,dc in directions:
                    nr,nc = i + dr, j + dc
                    

                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == 1:
                        
                        fresh -= 1
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                    
            minutes += 1
            

        return minutes if fresh == 0 else -1      
            

                        
