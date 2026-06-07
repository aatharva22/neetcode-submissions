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
        
        if not head:
            return None
        #populate hash map
        hmap = {}

        curr = head
        while curr:
            hmap[curr] = Node(curr.val)
            curr = curr.next
        
        #referencing new elements
        curr = head
        while curr:
            if curr.next:
                hmap[curr].next = hmap[curr.next]
            if curr.random:
                hmap[curr].random = hmap[curr.random]
            curr = curr.next
        start = hmap[head]
        return start

