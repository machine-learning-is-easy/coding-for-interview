

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        first, second = float("inf"), float("inf")

        def dfs(node):
            nonlocal first, second
            if not node:
                return
            else:
                if node.val < first:
                    first = node.val
                elif node.val < second and node.val != first:
                    second = node.val
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        if second != float("inf"):
            return second
        return -1