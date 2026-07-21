class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(i,j,setName):

            setName.add((i,j))

            for dr,dc in directions:

                nr,nc = i + dr, j + dc

                if 0<=nr<len(heights) and 0<=nc<len(heights[0]) and (nr,nc) not in setName and heights[nr][nc] >= heights[i][j]:

                    dfs(nr,nc,setName)
        

        #filling the pacific boundry

        for col in range(len(heights[0])):
            dfs(0,col,pacific)
        for row in range(len(heights)):
            dfs(row,0,pacific)

        #atlantic
        for col in range(len(heights[0])):
            dfs(len(heights) - 1,col,atlantic)
        for row in range(len(heights)):
            dfs(row,len(heights[0] )-1,atlantic)

        return [[i,j] for (i,j) in pacific & atlantic]


            