# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], tar: int) -> bool:

        if root is None:
            return False

        if root.val==tar and not root.left and not root.right:
            return True 
        tar-=root.val

        return self.hasPathSum(root.left,tar) or self.hasPathSum(root.right,tar)

        