# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = deque([root])
        root.val = 0

        while (q):
            size = len(q)
            level = []

            for i in range(size):
                node =q.popleft()
                level.append(node)

            level_sum=0
            for node in level:
                if node.left:
                    level_sum+=node.left.val
                if node.right:
                    level_sum+=node.right.val
            
            for node in level:

                sibling_sum = 0
                if node.left:
                    sibling_sum += node.left.val
                if node.right:
                    sibling_sum += node.right.val
                if node.left:
                    node.left.val  = level_sum - sibling_sum
                    q.append(node.left)

                if node.right:
                    node.right.val  = level_sum - sibling_sum
                    q.append(node.right)
        return root

                    