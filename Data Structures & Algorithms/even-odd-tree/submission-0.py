# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        q = deque([root])
        level = 0

        while q:

            prev = None

            for _ in range(len(q)):

                node = q.popleft()
                val = node.val

                # Even level: odd and strictly increasing
                if level % 2 == 0:
                    if val % 2 == 0:
                        return False

                    if prev is not None and val <= prev:
                        return False

                # Odd level: even and strictly decreasing
                else:
                    if val % 2 == 1:
                        return False

                    if prev is not None and val >= prev:
                        return False

                prev = val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            level += 1

        return True
            




            

            
        