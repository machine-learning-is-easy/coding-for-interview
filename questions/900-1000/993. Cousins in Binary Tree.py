
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        queue = [(root, None, 1)]
        x_node = None
        y_node = None

        while queue:
            node, parent, level = queue.pop(0)
            if node.val == x:
                x_node = (node, parent, level)
            elif node.val == y:
                y_node = (node, parent, level)

            if x_node is None or y_node is None:
                if node.left:
                    queue.append((node.left, node, level + 1))
                if node.right:
                    queue.append((node.right, node, level + 1))

        if x_node and y_node:
            return x_node[2] == y_node[2] and x_node[1] != y_node[1]
        else:
            return -1