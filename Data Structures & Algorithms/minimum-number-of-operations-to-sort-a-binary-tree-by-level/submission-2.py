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

            correct_position = sorted(level)
            position_dictionary = {val:i for i,val in enumerate(level)}

            for i in range(len(level)):
                if level[i]!=correct_position[i]:
                    j = position_dictionary[correct_position[i]]
                    level[i],level[j]=level[j],level[i]

                    position_dictionary[level[i]]=i
                    position_dictionary[level[j]]=j
                    ops+=1

        return ops               