

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        root.right, root.left = root.left, root.right
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root