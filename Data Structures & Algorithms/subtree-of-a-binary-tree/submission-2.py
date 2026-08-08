# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def sametree(self,root,p):
        if root is None and p is None:
            return True
        elif root is None or p is None:
            return False
        else:
            if root.val != p.val: return False
            return self.sametree(root.left,p.left) and self.sametree(root.right,p.right)
      
    def isSubtree(self, root: Optional[TreeNode], p: Optional[TreeNode]) -> bool:
        if root is None and p is None:
            return True
        elif root is None or p is None:
            return False
        else:
            if self.sametree(root,p) : return True
            return self.isSubtree(root.left,p) or self.isSubtree(root.right,p)

                
        



