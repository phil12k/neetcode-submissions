# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        ops=0

        while (q):
            size  = len(q)
            level = []

            for _ in range(size):
                
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            target = sorted(level)
            pos = {val:i for i,val in enumerate(level)}

            
            for i in range(len(level)):
                if level[i]!=target[i]:
                    j = pos[target[i]]

                    level[i],level[j]=level[j],level[i]

                    pos[level[i]]= i
                    pos[level[j]]=j
                    ops+=1

        return ops               