# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res=[]

        if not root:
            return ""

        q = deque([(root,chr(root.val + ord('a')))])

        while(q):
            node,path = q.popleft()

            if not node.left and not node.right:
                res.append(path)
            
            if node.left:
                q.append((node.left, chr(node.left.val + ord('a'))+path ))
            if node.right:
                q.append((node.right, chr(node.right.val + ord('a'))+path ))




        return min(res)