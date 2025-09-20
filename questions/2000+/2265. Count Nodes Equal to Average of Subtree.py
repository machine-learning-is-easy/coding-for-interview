

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                return 0, 0
            else:
                l_n, l_sum = dfs(node.left)
                r_n, r_sum = dfs(node.right)

                average = (l_sum + r_sum + node.val) // (l_n + r_n + 1)
                if node.val == average:
                    res.append(node.val)

                return l_n + r_n + 1, l_sum + r_sum + node.val

        dfs(root)
        return len(res)