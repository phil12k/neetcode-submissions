# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = []
        res1=[]

        def dfs(root,res):
            if not root :
                return 
            if not root.left and not root.right:    
                res.append(root.val)
            dfs(root.left ,res)
            dfs(root.right,res)

        dfs(p,res)
        dfs(q,res1)

        return res==res1