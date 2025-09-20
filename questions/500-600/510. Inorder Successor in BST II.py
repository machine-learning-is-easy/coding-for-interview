

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if not node:
            return None

        # Case 1: Node has a right subtree → find the leftmost node there
        if node.right:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr

        # Case 2: No right subtree → go up until node is a left child of its parent
        curr = node
        while curr.parent and curr == curr.parent.right:
            curr = curr.parent

        return curr.parent