
"""
tips: create two head, one is adding the node which is greater than x to next of the head, 
the other is adding the node which is greater than x to the next of the head.
iteration over the entire linked list
when current node is greater than x, move current node to the next of head2
when current node is lesser than x, move current node to the next of head1

end, add head2 next to the end of linked list1

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        head1 = ListNode()
        head2 = ListNode()

        cur = head
        cur1 = head1
        cur2 = head2

        while cur:
            if cur.val < x:
                cur1.next = cur
                cur1 = cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next

            cur = cur.next

        cur1.next = None
        cur2.next = None

        cur1.next = head2.next
        return head1.next