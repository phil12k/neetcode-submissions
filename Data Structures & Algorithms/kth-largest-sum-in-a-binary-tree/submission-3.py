# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        q = deque([root])
        i =0
        level_sum = []
        while(q):
            size = len(q)
            level = []


            for _ in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level_sum.append(sum(level))
            

        if len(level_sum)<k:
            return -1
        level_sum.sort()
        return level_sum[-k]

