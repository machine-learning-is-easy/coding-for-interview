

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def add(node1, node2):
            if not node1 and not node2:
                return None
            else:
                if node1:
                    val1 = node1.val
                else:
                    val1 = 0

                if node2:
                    val2 = node2.val
                else:
                    val2 = 0

                node_sum = TreeNode(val1 + val2)

                if node1 and node2:
                    node_sum.left = add(node1.left, node2.left)
                    node_sum.right = add(node1.right, node2.right)
                elif node1:
                    node_sum.left = add(node1.left, None)
                    node_sum.right = add(node1.right, None)
                elif node2:
                    node_sum.left = add(None, node2.left)
                    node_sum.right = add(None, node2.right)

                return node_sum

        return add(root1, root2)
