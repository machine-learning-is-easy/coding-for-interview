
class Solution:
    def __init__(self):
        self.nodes = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def add_inorder(node):
            if not node:
                return None
            add_inorder(node.left)
            self.nodes.append(node.val)
            add_inorder(node.right)

        add_inorder(root)
        return self.nodes

