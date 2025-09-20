

# breath first search algorithm
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        node_list = [root]

        # BFS search binary search tree
        while node_list:
            length = len(node_list)
            for ind in range(length):
                node = node_list.pop(0)

                if ind < length - 1:
                    node.next = node_list[0]

                if node.left:
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)
        return root


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = [root]
        while queue:
            pre = None
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

                if pre:
                    pre.next = cur
                pre = cur
        return root