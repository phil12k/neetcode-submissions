# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None:
            return False
        if q is None:
            return True

        if self.same(p,q):
            return True

        return self.isSubtree(p.left,q) or self.isSubtree(p.right,q)
        
    def same(self,p,q):
        if p is None:
            return not q
        if q is None:
            return not p
        if p.val!=q.val:
            return False
        return self.same(p.left,q.left) and self.same(p.right,q.right)
        