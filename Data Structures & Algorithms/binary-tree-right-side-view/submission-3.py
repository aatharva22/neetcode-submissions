# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #each levels last element is the answer
        # add each node to queue, and pop it, save last at each level
        # inorder traversal

        if not root:
            return []
        ans = []

        queue = deque([root])

        while queue:
            k = len(queue)
            for i in range(k):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if i == k - 1:
                    ans.append(node.val)
        return ans