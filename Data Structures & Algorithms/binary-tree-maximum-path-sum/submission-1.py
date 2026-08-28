# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # think a mix of bfs and kadanes algo
        self.maxSum = float("-inf")
        def lrsum(root):  # we want to call this on the left and right nodes
            if not root:
                return 0 
            
            left = lrsum(root.left)
            right = lrsum(root.right)
            self.maxSum = max(self.maxSum, left + right + root.val)

            return max(0, root.val + max(left, right))
        
        lrsum(root)
        return self.maxSum
        


          
            
        