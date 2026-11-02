# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        found_none = False
        q = deque([root])

        while(q):
            for i in range(len(q)):
                node = q.popleft()

                if node is None:
                    found_none = True

                else:
                    
                    if found_none:
                        return False

                        
                    q.append(node.left)
                    q.append(node.right)    

        return True    