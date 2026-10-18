# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        c = root.val
        l = 0

        def dfs(root,c):
            nonlocal l
            if root is None:
                return 
            
            if root.val>=c:
                l+=1
                c=max(c,root.val)
            dfs(root.left ,c)
            dfs(root.right,c)
        dfs(root,c)
        return l
        