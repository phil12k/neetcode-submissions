# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Map value -> index in inorder
        inorder_map = { value : i for i, value in enumerate(inorder) }

        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            # No elements in this subtree
            if left > right:
                return None

            # First element in preorder is the root
            root_val = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_val)

            # Find root position in inorder
            mid = inorder_map[root_val]

            # Build left subtree first
            root.left = build(left, mid - 1)

            # Then build right subtree
            root.right = build(mid + 1, right)

            return root

       

        return build(0 , len(preorder) - 1 )