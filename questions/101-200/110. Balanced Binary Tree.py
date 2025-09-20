


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced = True

        def dfs(node):
            nonlocal balanced
            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)
            if abs(left - right) > 1:
                balanced = False
            return 1 + max(left, right)

        dfs(root)
        return balanced