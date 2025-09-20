

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(node, path):
            nonlocal res
            if not node:
                return
            else:
                min_path = min(path)
                max_path = max(path)
                res = max([res, abs(node.val - min_path), abs(node.val - max_path)])

                path.append(node.val)
                dfs(node.left, path)
                dfs(node.right, path)
                path.pop(-1)

        dfs(root, [root.val])

        return res