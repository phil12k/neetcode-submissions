# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        if p is None:
            return q
        if q is None:
            return p

        p.val += q.val
        p.left = self.mergeTrees(p.left,q.left)
        p.right = self.mergeTrees(p.right,q.right)

        return p        