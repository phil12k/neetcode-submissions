class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        q = deque([root])

        while q:
            cur = q.popleft()

            if cur.val == head.val and self.sameT(head, cur):
                return True

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        return False

    def sameT(self, p, q):
        if p is None:
            return True
        if q is None:
            return False
        if p.val != q.val:
            return False

        return (
            self.sameT(p.next, q.left) or
            self.sameT(p.next, q.right)
        )
