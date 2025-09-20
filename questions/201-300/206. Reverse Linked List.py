
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reversed_head = None
        # original_head = head
        current_node = head
        while current_node:
             tmp_node = current_node  # Remember next node
             current_node = current_node.next

             tmp_node.next = reversed_head
             reversed_head = tmp_node

        return reversed_head