# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
   
    def isSubtree(self, root: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q is None:
            return True
        if root is None :
            return False
        if self.sameTree(root,q):
            return True
               
        return self.isSubtree(root.left,q) or self.isSubtree(root.right,q)


    def sameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        else:
            if p.val!=q.val:
                return False
            else:
                return self.sameTree(p.left,q.left) and self.sameTree(p.right, q.right)