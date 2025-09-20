

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        new_head = Node()
        cur = new_head

        def dfs(node):
            nonlocal cur
            if node is None:
                return None
            else:
                next_node = node.next

                cur.next = node
                node.prev = cur
                cur = cur.next
                if node.child:
                    dfs(node.child)
                    node.child = None
                # this node can be changed in the child process
                dfs(next_node)

        dfs(head)
        cur.next = None
        new_head = new_head.next
        new_head.prev = None
        return new_head

