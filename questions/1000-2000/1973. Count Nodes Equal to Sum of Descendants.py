

class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:

        count = 0

        def dfs(node):
            nonlocal count
            if not node:
                return 0
            else:
                l, r = dfs(node.left), dfs(node.right)
                if l + r == node.val:
                    count += 1
                return l + r + node.val

        dfs(root)
        return count