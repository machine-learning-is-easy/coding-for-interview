

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []

        def traverse_tree(root, depth):
            if root:
                if len(res) <= depth:
                    res.append(root.val)
                traverse_tree(root.right, depth + 1)
                traverse_tree(root.left, depth + 1)

        traverse_tree(root, 0)

        return res


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def dfs(node, level):
            if not node:
                return
            if len(res) < level:
                res.append(node.val)
            if node.right:
                dfs(node.right, level + 1)
            if node.left:
                dfs(node.left, level + 1)

        dfs(root, 1)

        return res
