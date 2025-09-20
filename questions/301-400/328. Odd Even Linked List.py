

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode()
        odd_cur = odd_head
        even_head = ListNode()
        even_cur = even_head

        cur = head
        sig = 0
        while cur:
            if sig == 0:
                odd_cur.next = cur
                odd_cur = odd_cur.next
                sig = 1
            else:
                even_cur.next = cur
                even_cur = even_cur.next
                sig = 0
            cur = cur.next

        odd_head = odd_head.next
        even_head = even_head.next

        odd_cur.next = even_head
        even_cur.next = None

        return odd_head