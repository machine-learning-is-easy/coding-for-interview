
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.max_length = 0

        def path_rout(node):
            # find the node max depth
            if node == None:
                return 0
            else:
                l = path_rout(node.left)
                r = path_rout(node.right)
                self.max_length = max(self.max_length, l + r + 1)
                return max(l, r) + 1

        path_rout(root)
        return self.max_length - 1

