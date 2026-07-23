# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node,a,b):
            
            if a.val<node.val and b.val < node.val:

                return dfs(node.left,a,b)
            
            elif (a.val>node.val and b.val > node.val) :

                return dfs(node.right, a, b)
            
            else:

                return node
        
        return dfs(root,p,q)