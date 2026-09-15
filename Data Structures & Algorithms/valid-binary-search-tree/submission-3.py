# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
               

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def dfs(low, root, high):
            if root is None:
                return True
            if not low<root.val<high:
                return False
            return dfs(low, root.left,root.val) and dfs(root.val, root.right, high)
            

        return dfs(float('-inf'), root, float('inf'))
        