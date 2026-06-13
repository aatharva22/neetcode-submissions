# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        ans = True

        def traverse(a,b):
            nonlocal ans
            if (a is None and b) or (b is None and a):
                ans =  False
                return
            elif a is None and b is None:
                return 
             
            if a.val != b.val:
                ans =  False
            traverse(a.left,b.left)
            traverse(a.right,b.right)
        traverse(p,q)
        return ans

            