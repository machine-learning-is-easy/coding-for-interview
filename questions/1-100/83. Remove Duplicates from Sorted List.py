
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        current = head
        # need to check next node and current node
        while current != None and current.next != None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
