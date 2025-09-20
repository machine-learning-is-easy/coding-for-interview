
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        visited = {}
        ind = 1
        node = head
        while node:
            if node is None:
                return True
            else:
                if id(node) in visited:
                    return visited[id(node)]
                else:
                    visited[id(node)] = node
            node = node.next

        return None