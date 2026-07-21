class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        #valid tree = all connected and no cycle

        #no cycle is edges 1 less than nodes

        if len(edges) >= n:
            return False
        
        hmap = {i:[] for i in range(n) }

        for a,b in edges:

            hmap[a].append(b)
            hmap[b].append(a)
        visited = set()
        
        def dfs(node):

            if node in visited:
                return
            visited.add(node)
            
            for n in hmap[node]:
                dfs(n)
        
        dfs(0)

        return len(visited) == n

