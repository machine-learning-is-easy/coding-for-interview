
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        head = TreeNode()
        tail = head

        def preorder(node):
            nonlocal tail
            if not node:
                return

            tail.right = node
            tail.left = None
            tail = tail.right

            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return head.right