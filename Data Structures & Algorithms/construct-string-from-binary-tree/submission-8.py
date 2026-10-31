# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        res = []
        if not root:
            return ""
        stack = [(root,False)]

        while stack:
            node , visited = stack.pop()

            if visited:
                res.append(")")
                continue
            
            res.append("(")
            res.append(str(node.val))
            stack.append((node,True))
            if node.right and not node.left:
                res.append("()")

            if node.right:
                stack.append((node.right,False))
            if node.left:
                stack.append((node.left,False))

        #dfs(root)
        result = "".join(res)
        return result[1:-1]