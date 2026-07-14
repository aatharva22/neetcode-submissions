"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        hmap = {}

        def dfs(old) -> Optional['Node']:

            if old in hmap:
                return hmap[old]
            
            copy = Node(old.val)
            hmap[old] = copy
            for n in old.neighbors:

                copy.neighbors.append(dfs(n))
            
            return copy
        
        return dfs(node)

