# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # what are the conditions for the binary tree to be the same
        # the curr values are the same
        # now what about if they are different
        # 1) the children could be uneven, like one node doesn't exist
        # 2) the children are even, but not equal. 
        # we should check everything first, then recurse
        if not p and not q:
            return True

        if (p and not q) or (q and not p) or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        