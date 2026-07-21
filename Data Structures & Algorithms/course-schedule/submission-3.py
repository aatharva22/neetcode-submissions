class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #creating adjacency matrix
        #if there is a cycle return False
        #if visiting is visited again -> cycle present

        hmap = {i:[] for i in range(numCourses)}

        for a,b in prerequisites:
            hmap[a].append(b)
        
        VISITING = 1
        VISITED = 2
        NOT = 0

        state = [NOT] * numCourses

        def checkCycle(node):

            if state[node] == VISITING:
                return True
            if state[node] == VISITED:
                return False
            state[node] = VISITING
            for neighbors in hmap[node]:

                if checkCycle(neighbors):
                    return True
            state[node] = VISITED        
            return False
        
        for i in range(numCourses):

            if checkCycle(i):
                return False
        return True

        


