# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        #post order
        # return, info passed up
        # operation :- each node adds the max depth of its left and right node

        def count(node):
            if not node:
                return 0
        
            left_depth = count(node.left)
            right_depth = count(node.right)

            self.diameter = max(self.diameter, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)
        count(root)
        return self.diameter

        