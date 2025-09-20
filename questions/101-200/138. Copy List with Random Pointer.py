

class Solution:

    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head):

        if head == None:
            return None

        p = head

        while p is not None:
            # clone the node
            node = Node(p.val, None, None)
            # change current nodes to the clone node
            p.next, node.next = node, p.next
            p = node.next

        # wire up clone node random pointer
        p = head
        while p is not None:
            if p.random is not None:
                p.next.random = p.random.next
            else:
                p.next.random = None
            p = p.next.next

        clone_head = head.next

        # restore original next pointer and change the clone next pointer
        p = head
        while p.next.next is not None:
            p.next.next, p = p.next.next.next, p.next.next

        return clone_head


# DFS version
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        mp = {}

        def duplicate_node(node):
            if id(node) in mp:
                return mp[id(node)]
            else:
                if node is None:
                    return None
                new_node = Node(node.val)
                mp[id(node)] = new_node
                new_node.next = duplicate_node(node.next)
                new_node.random = duplicate_node(node.random)
                return new_node

        new_head = duplicate_node(head)
        return new_head