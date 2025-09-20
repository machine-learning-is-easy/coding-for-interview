
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return []

        def contain1subtree(node):
            if node is None:
                return False
            else:
                leftcontain = contain1subtree(node.left)
                rightcontain = contain1subtree(node.right)

                if not leftcontain:
                    node.left = None
                if not rightcontain:
                    node.right = None

                return node.val == 1 or leftcontain or rightcontain

        contain1subtree(root)

        if root.left is None and root.right is None and root.val == 0:
            return None

        return root


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return 0
            else:
                l, r = dfs(node.left), dfs(node.right)

                if l == 0:
                    node.left = None
                if r == 0:
                    node.right = None

                if node.val == 1:
                    return l + r + 1
                else:
                    return l + r

        root_1 = dfs(root)
        if root_1 == 0:
            return None
        return root
