# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res=[]

        if root is None:
            return []

        while q:
            size = len(q)
            level = []
            for i in range(len(q)):
                node = q.popleft()
               # if node is None:
               #     return 
                level.append(node.val)
                

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
                
            res.append(max(level))
        
        return res

        