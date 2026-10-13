# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q is None:
            return True
        if p is None:
            return False
        if self.sameTree(p,q):
            return True
        return (self.isSubtree(p.left,q) or
                self.isSubtree(p.right,q) 
                 )


    def sameTree(self,p,q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            if p.val!=q.val:
                return False
            return (self.sameTree(p.left,q.left) and
                    self.sameTree(p.right,q.right) )           


        