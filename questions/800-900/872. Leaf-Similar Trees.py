
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return get_leaves(node.left) + get_leaves(node.right)

        return get_leaves(root1) == get_leaves(root2)