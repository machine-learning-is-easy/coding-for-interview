

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        insertNode = Node(insertVal)
        if not head:
            head = insertNode
            head.next = head
            return head

        cur, nxt = head, head.next
        maxNode, minNode = head, head.next  # 前后节点
        while True:
            if cur.val <= insertVal and insertVal <= nxt.val:  # 等于号
                cur.next = insertNode
                insertNode.next = nxt
                return head
            if cur.val > nxt.val:  # 大于号
                maxNode, minNode = cur, nxt
            cur = cur.next
            nxt = nxt.next
            if cur == head:
                break
        maxNode.next = insertNode
        insertNode.next = minNode
        return head


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        insert_node = Node(val=insertVal)
        if not head:
            return insert_node

        cur, nxt = head, head.next
        min_nod, max_nod = head, head.next
        while True:
            if insert_node.val <= nxt.val and insert_node.val >= cur.val:
                cur.next = insert_node
                insert_node.next = nxt
                return head

            if nxt.val < cur.val:
                min_nod, max_nod = nxt, cur

            cur, nxt = nxt, nxt.next
            if cur == head:
                break

        max_nod.next = insert_node
        insert_node.next = min_nod
        return head

# note: the ordered circular linked list does not need to count from head.

