

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        slowk = head
        fast = head

        for _ in range(k - 1):
            fast = fast.next
            slowk = slowk.next

        # find the last K
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.val, slowk.val = slowk.val, slow.val
        return head