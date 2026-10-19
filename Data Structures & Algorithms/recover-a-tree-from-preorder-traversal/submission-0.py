class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        pass
        parts = re.findall(r'-*\d+', traversal)
        i = 0

        def dfs(depth):
            nonlocal i

            if i >= len(parts):
                return None

            dashes = len(parts[i]) - len(parts[i].lstrip('-'))

            if dashes != depth:
                return None

            val = int(parts[i].lstrip('-'))
            i += 1

            node = TreeNode(val)
            node.left = dfs(depth + 1)
            node.right = dfs(depth + 1)

            return node

        return dfs(0)
