# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        val = None
        def inorder(node):
            nonlocal val
            nonlocal count
            if not node or val:
                return

            inorder(node.left)

            count += 1
            if count == k:
                val = node.val
            
            inorder(node.right)
        inorder(root)
        return val
            



            
