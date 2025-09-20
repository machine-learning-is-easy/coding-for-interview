
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0

        def dfs(node, maxv):
            nonlocal res
            if not node:
                return
            else:
                if node.val >= maxv:
                    res += 1

                max_sofar = max(maxv, node.val)
                dfs(node.left, max_sofar)
                dfs(node.right, max_sofar)

        dfs(root, float("-inf"))
        return res
