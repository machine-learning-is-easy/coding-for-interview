

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        node_a = {}
        curra = headA
        currb = headB
        while curra:
            node_a[curra] = curra.val
            curra = curra.next

        while currb:
            if currb in node_a:
                return currb
            else:
                currb = currb.next

        return None