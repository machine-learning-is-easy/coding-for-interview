

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        q_nodes = [root]
        while q_nodes:
            prev = None
            for _ in range(len(q_nodes)):
                current_node = q_nodes.pop(0)

                if current_node.left:
                    q_nodes.append(current_node.left)
                if current_node.right:
                    q_nodes.append(current_node.right)

                if prev:
                    prev.next = current_node
                    prev = prev.next
                else:
                    prev = current_node

            prev.next = None

        return root
