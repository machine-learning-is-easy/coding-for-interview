
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # If the root is None, return None
        if not root:
            return None

        # If the key to be deleted is less than the root's key,
        # then the function is recursively called with the left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # If the key to be deleted is greater than the root's key,
        # then the function is recursively called with the right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # If the root has no child or only one child, then the root is replaced with its child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # If the root has two children, then the inorder successor of the root is found
            else:
                node = root.right
                while node.left:
                    node = node.left
                # The value of the inorder successor is copied to the root
                root.val = node.val
                # The inorder successor is then deleted from the right subtree of the root
                root.right = self.deleteNode(root.right, node.val)

        return root