
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 1
        cur = p = head
        while cur.next: # need to be cur.next. every loop is checking the cur.next, not cur.
            size += 1
            cur = cur.next
            if size > n + 1:
                print(p.val)
                p = p.next

        if size == n: # head node is the last Nth node
            return head.next
        else:
            p.next = p.next.next
            return head


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur = head
        fast_cur = head
        slow_cur = head

        # move n + 1 times of fast_cur

        step = 1
        while fast_cur.next:
            fast_cur = fast_cur.next
            if step >= n + 1:
                slow_cur = slow_cur.next
            step += 1

        if step > n:
            slow_cur.next = slow_cur.next.next
        elif step == n: # if the head is the last Nth node
            head = head.next
        return head