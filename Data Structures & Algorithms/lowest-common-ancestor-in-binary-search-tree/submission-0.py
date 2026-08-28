# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # track first (bottom) occuracnes for
        # facts on BSTs. anything on the left of node can't be greater than it
        # anything on right can't be less then it
        # first condition, the curr node works
        if not root:
            return None
        
        if p.val >= root.val and q.val <= root.val or p.val <= root.val and q.val >= root.val:
            return root

        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        
        
