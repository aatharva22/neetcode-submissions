class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        count = 0
        
        graph = { i : [] for i in range(n)}

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(node):

            if node in visited:
                return
            else:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        dfs(neighbor)


        for i in range(n):

            if i not in visited:
                
                count += 1
                dfs(i)
        
        return count
            



        

        