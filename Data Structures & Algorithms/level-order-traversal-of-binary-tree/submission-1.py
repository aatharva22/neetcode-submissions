# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #in order traversal
        #operation on each node, add its left and right, and pop it, from queue
        #info passing top to bottom, in the queue

        if not root:
            return []
        queue = deque([root]) 
        ans = []

        while queue:
            subList = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                subList.append(node.val)
            ans.append(subList)
        return ans

