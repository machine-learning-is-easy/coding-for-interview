
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        stack = []
        current = prev.next

        for _ in range(right - left + 1):
            stack.append(current)
            current = current.next

        while stack:
            prev.next = stack.pop()
            prev = prev.next

        prev.next = current

        return dummy.next