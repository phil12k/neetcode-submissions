# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countPairs(self, root: Optional[TreeNode], tar: int) -> int:
        if not root:
            return 0

        count = 0
        stack = [(root, False)]
        depths = {}

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                if not node.left and not node.right:
                    depths[node] = [1]
                else:
                    left = depths.get(node.left, [])
                    right = depths.get(node.right, [])

                    for a in left:
                        for b in right:
                            if a + b <= distance:
                                count += 1

                    depths[node] = (
                        [d + 1 for d in left + right
                         if d + 1 < distance]
                    )

        return count