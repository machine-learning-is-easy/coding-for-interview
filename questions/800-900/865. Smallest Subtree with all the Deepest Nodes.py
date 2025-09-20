
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return 0, None
            else:
                l, r = dfs(node.left), dfs(node.right)

                if l[0] < r[0]:
                    return r[0] + 1, r[1]
                elif l[0] > r[0]:
                    return l[0] + 1, l[1]
                else:
                    return max(l[0], r[0]) + 1, node

        depth, node = dfs(root)
        return node