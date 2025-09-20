
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # need processing the first removeElements

        if not head:
            return head

        node = head

        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        # need to check the first node
        if head.val == val:
            head = head.next

        return head