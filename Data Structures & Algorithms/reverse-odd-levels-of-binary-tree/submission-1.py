# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = deque([root])
        odd=0

        while(q):
            size = len(q)
            level = []

            for _ in range(size):

                node = q.popleft()

                level.append(node)

                if node.left:
                    q.append(node.left)
               
                if node.right:
                    q.append(node.right)
            if odd%2==1:
                left=0
                right = len(level) - 1
    
                while left<right:
                    level[left].val, level[right].val= level[right].val, level[left].val
                    left+=1
                    right-=1
            odd+=1

        return root
        

            