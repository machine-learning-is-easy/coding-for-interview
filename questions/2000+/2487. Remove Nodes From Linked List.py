
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mono_stack = []
        cur = head
        while cur:
            while mono_stack and cur.val > mono_stack[-1].val:
                mono_stack.pop()
            mono_stack.append(cur)
            cur = cur.next

        head = ListNode()
        while mono_stack:
            node = mono_stack.pop(-1)
            node.next = head.next
            head.next = node
        return head.next

