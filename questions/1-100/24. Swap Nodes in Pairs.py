


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: return head

        if head.next:
            new_head = head.next
        else:
            new_head = head

        prev, cur, cur_next = None, head, head.next
        while cur and cur_next:
            next_ = cur_next.next
            if prev:
                prev.next = cur_next
            cur_next.next = cur
            cur.next = next_

            # change the pointer
            prev = cur
            if next_ and next_.next:
                cur = next_
                cur_next = cur.next
            else:
                break

        return new_head