

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        head = TreeNode()
        cur = head
        def inorder(node):
            nonlocal cur
            if not node:
                return None
            else:
                inorder(node.left)
                # need to change current node left.
                node.left = None
                cur.right = node
                cur = cur.right

                inorder(node.right)

        inorder(root)

        return head.right