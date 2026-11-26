# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        res=[]
        dfs(root)

        dif = float('inf')

        for i in range(0,len(res)-1):
            dif = min(res[i+1]-res[i],dif)

        return dif