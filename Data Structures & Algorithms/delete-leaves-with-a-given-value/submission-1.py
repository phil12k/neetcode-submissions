# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], tar: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        
        root.left = self.removeLeafNodes(root.left,tar)
        root.right = self.removeLeafNodes(root.right,tar)
        
        
        if root.left is None and root.right is None and root.val ==tar:
            return None
        
        return root
