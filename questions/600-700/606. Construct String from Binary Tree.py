

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node, s):
            if not node:
                pass
            else:
                s += [str(node.val)]
                if node.right:
                    s += ["("]
                    dfs(node.left, s)
                    s += [")"]

                    s += ["("]
                    dfs(node.right, s)
                    s += [")"]
                elif node.left:
                    s += ["("]
                    dfs(node.left, s)
                    s += [")"]

        s = []
        dfs(root, s)
        return ''.join(s)