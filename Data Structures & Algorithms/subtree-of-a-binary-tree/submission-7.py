# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            # here we should traveresse, then call is Same Tree
            def isSameTree(p, q):
                if not p and not q:
                    return True  #fix base case
                if not p or not q:
                    return False
                return p.val == q.val and isSameTree(p.right, q.right) and isSameTree(p.left, q.left)
            
            if not root:
                return False
            
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot) or isSameTree(root, subRoot)
            
                

        
        
        

        