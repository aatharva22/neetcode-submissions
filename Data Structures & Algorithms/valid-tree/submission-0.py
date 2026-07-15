class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        
       #connected and acyclic
       #acyclic :- edge count is n-1

        if len(edges) != n-1:
            return False


        graph = { i : [] for i in range(n)}

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        #to check is Connected
        visited = set()

        def dfs(node):

            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        
        dfs(0)

        return n == len(visited)
                
        

        


