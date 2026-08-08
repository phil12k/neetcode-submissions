# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    
    def isSameTree( self, root , q ):
        if root is None and q is None:
            return True
        elif root is None or q is None:
            return False
        else:
            if root.val != q.val:
                return  False
            return self.isSameTree(root.left,q.left) and self.isSameTree(root.right,q.right)
   
    def isSubtree(self, root: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if root is None and q is None:
            return True
        elif root is None or q is None:
            return False
        else:
            if self.isSameTree(root,q):
                return True
            else:
                return self.isSubtree(root.left,q) or self.isSubtree(root.right,q) 
    
           
