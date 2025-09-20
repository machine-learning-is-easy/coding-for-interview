

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        prev = float("inf")
        min_dif = float("inf")

        def dfs(node):
            nonlocal min_dif
            nonlocal prev
            if not node:
                return
            else:
                dfs(node.left)
                min_dif = min(abs(prev - node.val), min_dif)
                prev = node.val
                dfs(node.right)

        dfs(root)
        return min_dif