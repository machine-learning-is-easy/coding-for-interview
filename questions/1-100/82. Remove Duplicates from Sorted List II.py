
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, None)
        dummy.next = head
        prev = dummy
        cur = head
        while cur and cur.next:

            if cur.next.val == cur.val:
                # iteration to remove next node
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                cur.next, cur = None, cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next

        return dummy.next