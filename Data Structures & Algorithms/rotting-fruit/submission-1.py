class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        #Using BFS to return minimum minutes

        queue = deque()
        fresh = 0
        minutes = 0 
        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        while queue and fresh > 0:

            size = len(queue)

            # so even multiple rotten fruits can function together and only each layer will work
            for _ in range(size):

                r,c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == 1:
                        
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr,nc))

                        
            
            minutes += 1
        
        return -1 if fresh >0 else minutes


