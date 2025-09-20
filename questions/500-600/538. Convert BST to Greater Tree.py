

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        total = 0

        def dfs(node):
            nonlocal total
            if not node:
                return 0
            else:
                dfs(node.right)
                tmp = node.val
                node.val += total
                total += tmp
                dfs(node.left)

        dfs(root)
        return root