class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preReq = {i:[] for i in range(numCourses)}

        degree = [0] * numCourses
        for a,b in prerequisites:

            preReq[b].append(a)
            degree[a] += 1
        
        queue = deque(i for i in range(numCourses) if degree[i] == 0)

        order = []
        while queue:

            node = queue.popleft()
            order.append(node)

            for neighbor in preReq[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        
        return order if len(order) == numCourses else []
            
