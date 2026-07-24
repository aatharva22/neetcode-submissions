"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        seen = {}

        def createCopy(node):

            if not node:
                return None
            if node in seen:
                return seen[node]
            
            copy = Node(node.val)
            seen[node] = copy

            copy.next = createCopy(node.next)
            copy.random = createCopy(node.random)

            return copy
        
        return createCopy(head)


        










