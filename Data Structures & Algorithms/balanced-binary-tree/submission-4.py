# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        check = True 
        def height(node):
            nonlocal check
            if not node:
                return 0
            
            
        
            height_left = 1 + height(node.left)
            height_right = 1 + height(node.right)

            if abs(height_left - height_right) > 1:
                check = False
            return max(height_left, height_right)
                
        height(root)
        return check       
    
    
        