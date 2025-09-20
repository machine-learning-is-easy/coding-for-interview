

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        queue = [(root, 1)]

        while queue:
            node, dpth = queue.pop(0)
            if dpth == depth - 1:
                new_left_node = TreeNode(val)
                tmp = node.left
                node.left = new_left_node
                new_left_node.left = tmp

                new_right_node = TreeNode(val)
                tmp = node.right
                node.right = new_right_node
                new_right_node.right = tmp
            elif dpth <= depth - 1:
                if node.left:
                    queue.append((node.left, dpth + 1))
                if node.right:
                    queue.append((node.right, dpth + 1))

        return root

