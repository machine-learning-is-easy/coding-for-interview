

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right:  # It's a leaf
                return node.val if is_left else 0
            return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root, False)