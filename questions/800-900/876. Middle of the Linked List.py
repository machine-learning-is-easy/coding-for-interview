
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if not fast.next:
                break
            fast = fast.next

        return slow