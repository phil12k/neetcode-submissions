"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        if not root:
            return []

        for child in root.children:
            res.extend(self.postorder(child))

        res.append(root.val)

        return res