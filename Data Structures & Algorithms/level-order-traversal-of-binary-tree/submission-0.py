# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        if not root:
            return []
        queue = deque([root])

        while queue:
            level = len(queue)
            current_list = []
            for _ in range(0,level):
                node = queue.popleft()
                current_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(current_list)
        return ans


        