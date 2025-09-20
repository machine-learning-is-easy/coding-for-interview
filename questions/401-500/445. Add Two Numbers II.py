
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # find the length of both lists
        n1 = n2 = 0
        v1 = 0
        v2 = 0
        curr1, curr2 = l1, l2
        while curr1:
            v1 = v1 * 10 + curr1.val
            curr1 = curr1.next
            n1 += 1

        while curr2:
            v2 = v2 * 10 + curr2.val
            curr2 = curr2.next
            n2 += 1

        totalvl = v1 + v2

        val_string_list = [c for c in str(totalvl)]

        head = ListNode()
        cur = head
        for _ in val_string_list:
            cur.next = ListNode(int(_))
            cur = cur.next

        return head.next


# alternative solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1_array = []
        cur_head1 = l1
        while cur_head1:
            node1_array.append(cur_head1.val)
            cur_head1 = cur_head1.next

        node2_array = []
        cur_head2 = l2
        while cur_head2:
            node2_array.append(cur_head2.val)
            cur_head2 = cur_head2.next

        carry = 0
        idx1 = len(node1_array) - 1
        idx2 = len(node2_array) - 1

        head = None
        while idx1 >= 0 or idx2 >= 0:
            if idx1 >= 0:
                val1 = node1_array[idx1]
            else:
                val1 = 0

            if idx2 >= 0:
                val2 = node2_array[idx2]
            else:
                val2 = 0

            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10

            node = ListNode(val)
            node.next = head
            head = node

            idx1 -= 1
            idx2 -= 1

        return head