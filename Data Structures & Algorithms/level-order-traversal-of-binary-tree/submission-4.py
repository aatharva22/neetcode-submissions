# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        queue = deque()
        ans = []
        if root:
            queue.append(root)
        
        while queue:

            

            temp = []
            length = len(queue)
            for i in range(length):
                if len(queue) != 0:
                    node = queue.popleft()
                else:
                    break
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                
                temp.append(node.val)
            ans.append(temp)
            
        
        return ans

                

