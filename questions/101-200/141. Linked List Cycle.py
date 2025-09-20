

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # question: to be clear all the nodes are connected. if not all connected, need to traverse all nodes.
        # if can divided into 2 segments. need to iteration over all the nodes using dfs
        if head is [None]:
            return True

        nodes = {}
        while head != None:
            if id(head) in nodes:
                return True
            nodes[id(head)] = head
            head = head.next
        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mp = set()
        def detect_cycle(node):
            if node is None:
                return False
            elif id(node) in mp:
                return True
            else:
                mp.add(id(node))
                return detect_cycle(node.next)
        return detect_cycle(head)