


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst = []
        tmp = head
        while tmp:
            lst.append(tmp.val)
            tmp = tmp.next

        res = []
        for i in range(0, len(lst), k):
            t = lst[i:i + k]
            if len(t) == k:
                res += t[::-1]
            else:
                res += t

        dummy = ListNode(0)
        temp = dummy
        while len(res) != 0:
            temp.next = ListNode(res.pop(0))
            temp = temp.next
        return dummy.next