
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        inorder_seq = []

        def inorder(node):
            if node is None:
                return
            else:
                inorder(node.left)
                if len(inorder_seq) < k:
                    inorder_seq.append(node.val)
                else:
                    return
                inorder(node.right)

        inorder(root)
        return inorder_seq[-1]