
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode()
        cur = head
        list_cur = lists

        while list_cur:
            # find the min_index
            min_index = 0
            for ind in range(len(list_cur)):
                if list_cur[ind].val < list_cur[min_index].val:
                    min_index = ind

            cur.next = list_cur[min_index]
            cur = cur.next

            if list_cur[min_index].next:
                list_cur[min_index] = list_cur[min_index].next
            else:
                list_cur.pop(min_index)

        return head.next
