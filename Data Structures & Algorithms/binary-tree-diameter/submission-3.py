# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxL = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def diameter(node):

            if not node:
                return 0
            left_depth = diameter(node.left)
            right_depth = diameter(node.right)
            self.maxL = max(self.maxL, left_depth + right_depth)
            return 1 + max(left_depth,right_depth)

        diameter(root)
        return self.maxL
