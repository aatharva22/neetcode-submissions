# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #operation :- get heights of left and right and computer diff
        #information passed from child to parent, so each node returns its maxHeight
        #post order
        
        ans = True

        def valid(node):
            nonlocal ans

            if not node:
                return 0
            
            #get info from children
            left_depth = valid(node.left)
            right_depth = valid(node.right)

            #operation
            if abs(left_depth - right_depth) > 1:
                ans = False
            
            return 1 + max(left_depth, right_depth)
        
        valid(root)
        return ans
