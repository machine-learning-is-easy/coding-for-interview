# 2 add two number, two number are stored in two list

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode()
        p = l1
        q = l2
        curr = head
        carry = 0
        while p != None or q != None:
            # checking the current value of p and q
            if p != None:
                pv = p.val
            else:
                pv = 0

            if q != None:
                qv = q.val
            else:
                qv = 0
            cv = (pv + qv + carry) % 10
            carry = int((pv + qv + carry - cv) / 10)

            # move the result pointer current node
            curr.next = ListNode(cv)
            curr = curr.next

            # move to the next pointer
            if p != None:
                p = p.next
            if q != None:
                q = q.next

        # deal with the very last carry value
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next
