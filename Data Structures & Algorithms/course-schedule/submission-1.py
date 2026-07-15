class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create adjacency list

        graph = {i : [] for i in range(numCourses)}

        for a,b in prerequisites:
            graph[a].append(b)

        NOT,VISITING,VISITED = 0,1,2
        state = [NOT] * (numCourses)
        def hasCycle(node) -> bool:

            if state[node] == VISITING:
                return True
            if state[node] == VISITED:
                return False
            state[node] = VISITING

            for neighbor in graph[node]:

                if hasCycle(neighbor):
                    return True
            
            state[node] = VISITED
            return False

        
        for i in range(numCourses):
            if hasCycle(i):
                return False
        return True




