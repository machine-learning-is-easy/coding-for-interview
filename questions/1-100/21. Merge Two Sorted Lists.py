
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        head = ListNode()
        cur = head
        while p1 != None or p2 != None:
            if p1 == None:
                cur.next = p2
                cur = cur.next
                p2 = p2.next
            elif p2 == None:
                cur.next = p1
                cur = cur.next
                p1 = p1.next
            elif p1.val < p2.val:
                cur.next = p1
                cur = cur.next
                p1 = p1.next
            else:
                cur.next = p2
                cur = cur.next
                p2 = p2.next
        return head.next