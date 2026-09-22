# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(node):
            if node is None:
                result.append("N")
                return

            result.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(result)

    def deserialize(self, data):
        values = iter(data.split(","))

        def dfs():
            value = next(values)

            if value == "N":
                return None

            node = TreeNode(int(value))

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


