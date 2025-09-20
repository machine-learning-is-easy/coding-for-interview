

# tricky version
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        successor = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor

# intuitive version is get all the list of inorder nodes, then find the successor of the selective node.

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        self.successor = None

        def inorder(root):
            if not root:
                return False
            if root.val > p.val:  # if p.value is greater than current node, no need to search left branch
                inorder(root.left)

            if root.val > p.val and not self.successor:
                self.successor = root
            inorder(root.right)

        inorder(root)
        return self.successor