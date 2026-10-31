# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal = True
        def dfs(root):
            nonlocal bal
            if not root:
                return 0
            left  =  dfs(root.left)
            right =  dfs(root.right)

            if  abs(left-right)>1:
                bal = False
            return 1 + max(left,right)

        k = dfs(root)

        return bal
        