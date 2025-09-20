31.	Linked list
Tips. 
1.	For node merge, normally create an empty node, adding nodes to the next node of the empty node. When finish operation, return the empty node.next
2.	Use node address id(node) and hash table 
3.	normally find the tail or the node before the linked list if the operation
4.	Fast and slow pointer to get node from the end.
5.	Pay attention it condition to iteration the linked list, cur or cur.next
6.	When operating the ith node, normally find the processor node of the ith node in a single linked list. Also, we use the previous node to do the operation, but the previous node needs to be processed as well.
7.	Linked lists can be used DFS algorithm.
8.	Sort linked list
9.	LRU

Questions:
1.	Length of linked list.
2.	Duplicate elements, if there is no duplicate element, we can use the value as the key in the hash table. 
3.	Do we need to create a new linked list, or we can change the linked list in place?


a.	Single linked list
2. Add Two Numbers (apply to many cases)
Tips: It is about adding two digits in a linked list into one linked list. It is not difficult but need to think about all the conditions. 1. The two linked lists are not the same length. Deal with the situation when any of the linked lists is exhausted.  2. Deal with the operation and save the result. 3. Move to the next pointer. 4 deal with the final state of the result.

Another variation is the first node is the most significant digit, the last node is the least significant digit. 

24. Swap Nodes in Pairs
TIPS: keep prev, cur, cur_next nodes. save the cur_next before operation. Switch cur, cur_next node, update the prev, cur, cur_next nodes at the end of the each loop.

138. Copy List with Random Pointer
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        mp = {}

        def duplicate_node(node):
            if id(node) in mp:
                return mp[id(node)]
            else:
                if node is None:
                    return None
                new_node = Node(node.val)
                mp[id(node)] = new_node
                new_node.next = duplicate_node(node.next)
                new_node.random = duplicate_node(node.random)
                return new_node

        new_head = duplicate_node(head)
        return new_head

876. Middle of the Linked List
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if not fast.next:
                break
            fast = fast.next

        return slow

203. Remove Linked List Elements
TIPS: because is a directional linked list, only traverses from head to tail. The point needs to operational node previous node.
Normally, check all head.next node. If head.next node is equal to the val, remove the head next node. Becareful, the head node is not checked. 

19. Remove Nth Node from End of List
Two pointers, P, and cur, cur move to the next n steps, and after n + 1 steps, P and cur move to the next node together. When cur reach the end of the linked list. P is the previous node of the last nth node from the end.
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 1
        cur = p = head
        while cur.next:
            size += 1
            cur = cur.next
            if size > n + 1:
                print(p.val)
                p = p.next

        if size == n:
            return head.next
        else:
            p.next = p.next.next
            return head

1721. Swapping Nodes in a Linked List
TIPS: find the first K node. Iteration k – 1 steps from head. Then move fast from Kth nodes and slow pointer from head until fast point.next is None. Then find the first K node and last K node. Replace the two nodes value. 

206. Reverse Linked List (Easy)
TIPS: set up three variables. Head, reverse_head, and current node. The head is always pointing to the head of the original list. reverse_head points to the reversed linked list. The current node is pointing to the node poped up. 
Head = node.next. # move the head to next node. 
Node.next = reverse_head
Reverse_head = node.

21. Merge Two Sorted Lists (Easy)
TIPS: two pointers head1, head2 to the heads of the sorted list. merge_head point to the head of merged linked list
Compare the head1.value and head2 value, get the lower node and current_node = head with lower value. The lower value head move next node
Push current_node to the head of merged linked list.
Current_node.next = merge_head
Merge_head = current_node

61. Rotate List
Pay attention that the rotation times are longer than the length of the linked list
TIPS: first find the length of the list and the tail of the linked list. connect tail.next to the head. Find the new head is Length - K%length, tail is Length – K % length – 1. Find the tail. Assign the new head to tail.next. tail.next = None break the circle.

Edge case:
Root is None, linked list node number is 1.
Rotation number is greater than the length of the linked list

24. Swap Nodes in Pairs (Medium)
160. Intersection of Two Linked Lists (Easy)
Question: ordered or not ordered?
234. Palindrome Linked List (Easy)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        global front
        front = head

        def helper(back) -> bool:
            global front
            if not back:
                return True

            # let back pointer travel to the back of the list through recursion
            equal_so_far = helper(back.next) 
	   # check the second node and last 2 element.

            # check if front and back have the same value
            value_equal = (front.val == back.val)

            # when the function return, back is gradually moved toward head of the list
            # move front accordingly to compare their value
            front = front.next
            return equal_so_far and value_equal

        return helper(head)

TIPS: iterative all next until to reach the last element, then check the two values. Then move the front to the next.

1265. Print Immutable Linked List in Reverse
class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:

        res = []

        def dfs(node):
            if not node:
                return
            else:
                dfs(node.getNext())
                res.append(node.printValue())

        dfs(head)
        return res

83. Remove Duplicates from Sorted List (Easy)
328. Odd Even Linked List (Medium)
这道题其实很简单，千万不要把题目复杂化。

82. Remove Duplicates from Sorted List II
TIPS: prev, cur and cur.next. check if cur.val == cur.next.val. if yes, move cur to last element which value is the same. Move cur = cur.next. prev.next = cur. Move prev = prev.next
148. Sort List (Medium)
利用快慢指针找到链表中点后，可以对链表进行归并排序

92. Reverse Linked List II
TIPS: 1. Find the previous node prev, 2 reverse the nodes between two nodes, add the nodes to a stack 3. Pop the stack nodes, append the nodes to the next of prev. 4. Append the rest of the linked list node to the end. 

25. Reverse Nodes in k-Group
TIPS: put the nodes into a list. Reverse k element in the list. connect the node again.


148. Sort List
TIPS: split linked list. And merge two linked list

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        dummy = ListNode()
        cur = dummy
        while left and right:
            if left.val < right.val:
                cur.next = left
                cur = cur.next
                left = left.next
            else:
                cur.next = right
                cur = cur.next
                right = right.next
        cur.next = left or right

        return dummy.next

b.	Circular linked list

c.	Double linked list
Convert a tree to double linked list
Priority queue using double linked list
Reverse every k node in double linked list
146. LRU Cache: https://leetcode.com/problems/lru-cache/
class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1

        # move the accessed node to the head;
        self._move_to_head(node)

        return node.value

    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def put(self, key: int, value: int) -> None:

        node = self.cache.get(key)
        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
   	self._add_node(newNode)
      	self.size += 1
     	if self.size > self.capacity:
         		# pop the tail
        		tail = self._pop_tail()
        		del self.cache[tail.key]
       		self.size -= 1
     else:
        # update the value.
        node.value = value
       self._move_to_head(node)

step 1. Create node structure with key, value, previous pointer, and next pointer.
step 2. Define the LRU __init__ function, need capacity as parameter, create self.size, self.capacity, self.cache, self.head, self.tail.
step 3. Define put. The input parameter has a key and value. First need to check if the current key in the cache, if yes, update the node value with the new value, delete the current node, and put the current node to the head.next. if No. create a node with key and value and put the node in the cache. Increase the size. Put the node to the head.next. Then compare the size with the capacity, if the size is greater than the capacity, remove the tail node, and remove the tail node from the hash table.

706. Design HashMap
TIPS: list + linked list to implement the hashmap
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size
    def _index(self, key: int) -> int:
        return key % self.size
    def put(self, key: int, value: int) -> None:
        idx = self._index(key)
        if not self.table[idx]:
            self.table[idx] = ListNode(key, value)
            return
        current = self.table[idx]
        while current:
            if current.key == key:
                current.value = value
                return
            if not current.next:
                current.next = ListNode(key, value)
                return
            current = current.next
    def get(self, key: int) -> int:
        idx = self._index(key)
        current = self.table[idx]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        idx = self._index(key)
        current = self.table[idx]
        if not current:
            return
        if current.key == key:
            self.table[idx] = current.next
            return
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
