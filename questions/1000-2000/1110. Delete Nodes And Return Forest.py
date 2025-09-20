

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        res = []

        def dfs(node):
            nonlocal to_delete
            if not node:
                return None
            else:
                left_node = node.left
                right_node = node.right
                # need to resign the node.left and node.right.
                if node.left:
                    node.left = dfs(node.left)
                if node.right:
                    node.right = dfs(node.right)

                # need to return the current node value
                if node.val in to_delete:
                    if left_node and left_node.val not in to_delete:
                        res.append(left_node)
                    if right_node and right_node.val not in to_delete:
                        res.append(right_node)
                    return None
                else:
                    return node

        dfs(root)
        if root.val not in to_delete:
            res.append(root)
        return res