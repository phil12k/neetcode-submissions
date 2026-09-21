# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.res = root.val

        def dfs(root):
            if root is None:
                return 0

            right = max(0, dfs(root.right))
            left  = max(0, dfs(root.left))

            current = left + root.val + right
            self.res = max(current, self.res)
            return root.val + max(left, right)

        dfs(root)
        return self.res


        