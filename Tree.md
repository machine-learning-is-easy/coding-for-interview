# Tree
## Key Points:
DFS, BFS search the tree, DFS search the tree, try left branch, right branch, then process current node, from the question, define dfs left branch, dfs right branch return type and value.  The global variable to save the result current node, left branch returns, right branch returns. And return the result of current node (should be same with left branch and right branch returns, including current node)
1.	If modifying a tree pointer, like Converting a tree to a linked list or double-linked list, need to keep the record of the left and right child before changing the current node pointer. The recursive function needs to return the current node.
2.	If validating the nodes, needs to return True or False, and node processing needs to check the left child and right child results.
3.	Adding parameters in the traverse function of a tree, like depth, or node path to the parameter of the recursive function.
4.	Be careful the recursive function return condition. node.left and node.right are None OR node is None
5.	Left branch, right branch, current node or current node, left branch, right branch depends on logic of return value, Current_node.left = recursive(current_node.left) 
# It may change the current tree or create a tree. In that case, need to save it to a temp variable.
6.	Return value, return current node or Boolean. May need a global variable to save the value
7.	Tree traverse can work together with a list, hash table (dictionary, set), and linked list. 
8.	If changing the node pointer left, and right in place, need to save the left, and right children nodes to temporary variables, and recursively call the saved left, and right variables, otherwise the left and right may be changed.
9.	If changing the tree to a linked list, need to create an empty node as head, assign tail to head, and add all the nodes in certain order to the tail.
10.	Binary Tree vs Binary Search Tree. The difference is the order.
11.	BFS vs Recursive function. If operating nodes at the same level need BFS, if depth question, Recursive function (DFS).
12.	Tree + hash table. Put the BT nodes into a hashtable. The key of the hashtable is the index of the nodes. the parent node can be found by the index of the leaf.
13.	Left view, right view and boundary of the Binary Tree.
14.	Find all leaves in a tree (366)
15.	Be careful, if change the node left and right point in the DFS, need to save it. For later operation.
16.	Delete the node in tree.
17.	Return condition is node is None or node.left is None and node.right is None
18.	Keep the previous node when validating a graph is a tree.
19.	Path problem. Process current node, left child, right child. Because left and right child is not linked together. When finish left need to remove the left child node from hashtable or stack.
20.	Max path sum or production. For a dfs iteration. Need to max(dfs(node.left), 0) for maximum sum and max(dfs(node.left), 1) for maximum product. 
21.	DFS Find the path of the nod. For example, Find K distance from a Node
22.	Completeness of the tree. BFS search from the root of the tree. Adding left and right to the queue, once encounter a None in the queue, rest of the element need to None.
23.	Collecting apples

Questions:
1.	Has negative values or zero values? like path sum to target?
2.	What is the tree is None?

Mistakes: processing node value, left child value, and right child value in the process. left child value and right child value need to be called recursively. The processing of inorder, preorder and postorder only process one node.


## a.	Common ancestor
Questions: does the node have duplicate values?
DFS searches the tree from the root and keeps the path as a parameter in the DFS function. If find the node A path, save it to a variable, if find the node B path, save it to another variable. Then compare two nodes list, the last node which is the same in the two lists is the common ancestor of the two nodes.

Variation 1: if binary search tree. The left child node value is less than the root, right child nodes are greater than the root. Only if both node A value and node B value are less than the current node, search the left subtree. If both node A value and node B value are greater than the current node value, search the right subtree.

Variation 2: searching two nodes, the nodes have parent pointers. We can start from the node, searching upwards to find the path of p, q 
### 1123. Lowest Common Ancestor of Deepest Leaves
1.	Return result if node is None
2.	Call left and right child node
3.	Assume find the left deepest common ancestor and right child deepest common ancestor. Check left and right level, if left depth is greater, use left value, if right level is greater user right value, pass the left value or right value back to processor call. if left depth and right depth, return current node.

```python
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return 0, None
            l, r = dfs(node.left), dfs(node.right)
            if l[0] > r[0]:
                return l[0] + 1, l[1]
            if l[0] < r[0]:
                return r[0] + 1, r[1]
            return l[0] + 1, node
        return dfs(root)[1]
```
### 235. Lowest Common Ancestor of a Binary Search Tree
TIPS: we can determine go left or go right branch in BST after comparing the current node value and the two value. because of BST, if both value < node.value, go left, if both value > node.value. go right. If one is less than the node.value and the other is greater than node.value. current value is the common ancestor.
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
```

### 236. Lowest Common Ancestor of a Binary Tree
TIPS: dfs search the left branch and the right branch. Check if left branch or right branch finds any node. 

### 1650. Lowest Common Ancestor of a Binary Tree III
It is different from others, the nodes can access the parent node, then traverse the parent node, from first node, get the path, then traverse the current node and parent node for the second node, if find a node in the first node path, the node is the lowest common ancestor. Need to start traverse from the current node

### 1483. Kth Ancestor of a Tree Node
TIPS: BFS search the tree. Find the path from root to the node. Keep the path as well. The Kth ancestor is [-K] element of the path.
OR: convert the tree to graph, key is the node, and the value is the parent node. The Kth ancestor need DFS search the node K times.

### 863. All Nodes Distance K in Binary Tree

TIPS:
Find the path the node in the Tree, keep record of the path. last element of the path is the node, iteration from the path from the end to the beginning, step = 0, find all the elements of the path with distance K-step.
```python
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # (find_node, distance)
        # edge case on root and target
        if not root:
            return []

        res = []

        def find_nodes(node, depth):
            if not node:
                return

            if depth >= 0:
                if node.val not in res and depth == 0 and node.val not in visited:
                    res.append(node.val)
                visited.add(node.val)
                find_nodes(node.right, depth - 1)
                find_nodes(node.left, depth - 1)
            else:
                return

        path = []

        def find_path(node, tmp):
            nonlocal path
            nonlocal target
            if not node:
                return
            tmp.append(node)
            if node.val == target.val:
                path = list(tmp)
            else:
                find_path(node.left, tmp)
                find_path(node.right, tmp)
            tmp.pop(-1)

        find_path(root, [])
        step = 0
        visited = set()
        while path:
            node = path.pop(-1)
            find_nodes(node, k - step)
            step += 1
        return res
```

### 1740. Find Distance in a Binary Tree
The return of DFS needs to have two variables. 1 is if find any node, the second is depth to the node. Postorder search the dfs. Check left branch, check the right branch. if current node is in the branch. check if any left and right branch find the other node. If yes, return 2, and the distance.
If current node does not in the targets. Check if the left or right branch return got two nodes. if got two nodes, just return left or right branch return. If any of them find one node, just return the branch, but depth need to plus 1. If neither of the branch return find the nodes, just return 0, 0.

Another version:
Find the LCA of the two nodes. then from the node, BFS search and find the two paths of the nodes.
Another version:
Find the path of P, and the path of Q.  find the different paths between P and Q. then the distance can be calculated by the length(d_p – d_q)

### 1644. Lowest Common Ancestor of a Binary Tree II
Find the node and lowest common ancestor.
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        values = set([p.val, q.val])
        def dfs(node):
            if not node:
                return 0, None
            else:
                l, r = dfs(node.left), dfs(node.right)
                if node.val in values:
                    return l[0] + r[0] + 1, node
                else:
                    if l[0] == 2:
                        return l
                    elif r[0] == 2:
                        return r
                    else:
                        return l[0] + r[0], node
        matched, node = dfs(root)
        if matched == 2:
            return node
        else:
            return None
```
### 124. Binary Tree Maximum Path Sum (any path in the Binary Tree)
Tips: recursive function, the parameter is the node. Return 0 if the node is None. Then calculate the right child maximum sum from root to leave L, left maximum sum from root to leaves R, and the maximum path in this node is max (maximum path, value + L + R). return max (R, L) + node.value. Becareful the maximum value does not necessary include left child or right child.  So need to be maximum(max_gain(node.left), 0). But the return value needs to add current node. Return value need to be node.val + max(left, right,0)
```python
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # **********
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0

            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # the price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain

            # update max_sum if it's better to start a new path
            max_sum = max(max_sum, price_newpath)

            # for recursion : return current tree maximum gain, need to include 
            # current node.
            return node.val + max(left_gain, right_gain, 0)

        max_sum = float('-inf')
        max_gain(root)
        return max_sum
```

### 2096. Step-By-Step Directions from a Binary Tree Node to Another
TIPS: typical answer LCA + BFS. find the root with the local common ancestor. BFS search from the root. 
```python
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def lca(node):
            # """Return lowest common ancestor of start and dest nodes."""
            if not node or node.val in (startValue, destValue):
                return node
            left, right = lca(node.left), lca(node.right)
            return node if left and right else left or right

        root = lca(root)  # only this sub-tree matters

        ps = pd = ""
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            if node.val == startValue: ps = path
            if node.val == destValue: pd = path
            if node.left: stack.append((node.left, path + "L"))
            if node.right: stack.append((node.right, path + "R"))
        return "U" * len(ps) + pd
```
### 1676. Lowest Common Ancestor of a Binary Tree IV
TIPS: is not known if the given nodes are in the tree.
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        node_len = len(nodes)

        node_val = set([node.val for node in nodes])

        def dfs(node):
            if not node:
                return 0, node
            l, r = dfs(node.left), dfs(node.right)

            if node.val in node_val:
                return l[0] + r[0] + 1, node
            else:
                if l[0] == node_len:
                    return l
                if r[0] == node_len:
                    return r
                return l[0] + r[0], node
        
        return dfs(root)[1]
```

### 1443. Minimum Time to Collect All Apples in a Tree
TIPS: this is quite typical. converting the edges into a graph. Traverse the graph from 0 nodes. DFS return -1, not find an apple. If returns 0 or others, it means left or right has the apple. Should add the steps from left or right. And return the total amount of them.
```python
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # define DFS function
        def dfs(node):
            visited.add(node)
            ct = 0
            for nxt_node in graph[node]:
                if nxt_node not in visited:
                    steps = dfs(nxt_node)# DFS to searching child branch
                    if steps != -1:
                        ct += 2
                        ct += steps
            if hasApple[node] or ct > 0: # return ct.
                return ct
            return -1

        # convert the edges into graph
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        visited = set()

        steps = dfs(0)
        if steps == -1:
            return 0
        else:
            return steps
```

## b.	Invert/Flip Binary Tree
TIPS: invert left and right subtree. Continue to invert left and right subtree
 
## c.	Validate Binary Search Tree
### 98. Validate Binary Search Tree: https://leetcode.com/problemset/all/?status=AC&page=2

Tips: add min and maximum to the recursive function
## d.	Construct Binary Tree from Preorder and Inorder Traversal

## e.	536. Construct Binary Tree from String
TIPS: create a mapper of (and) index. It helps to locate the right), and split the string. and DFS to split the entire problem into sub problem.
```python

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        d = collections.defaultdict(int)
        stack = []
        for i, c in enumerate(s):
            if c == "(": stack.append(i)
            if c == ")": d[stack.pop()] = i

        def get_tree(l: int, r: int) -> Optional[TreeNode]:
            if l > r: return None

            val = []
            while l <= r and s[l] != "(":
                val.append(s[l])
                l += 1
            node = TreeNode(int("".join(val)))
            if l >= r: return node

            left_l_p = l
            left_r_p = d[left_l_p]
            node.left = get_tree(left_l_p + 1, left_r_p - 1)

            right_l_p = left_r_p + 1
            right_r_p = d[right_l_p]
            node.right = get_tree(right_l_p + 1, right_r_p - 1)

            return node

        return get_tree(0, len(s) - 1)
```
## f.	Convert a tree into a double-linked list.
TIPS: normal traverse the tree as required. Keep the head and tail of the linked list. for the current node, need to add the current node to the tail.

### 114. Flatten Binary Tree to Linked List
```python
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        head = TreeNode()
        tail = head

        def preorder(node):
            nonlocal tail
            if not node:
                return

            left_branch = node.left
            right_branch = node.right

            tail.right = node
            tail.left = None
            tail = tail.right

            preorder(left_branch)
            preorder(right_branch)

        preorder(root)
        return head.right
```
TIPS: define an empty node as a linked list head (this is a very common operation). Assign head to tail variable. We will append a node from the tree to the tail. Preorder traverses all the nodes in the tree. Processing the tree with preorder sequence. Root, left branch, right branch. Because it will change the left and right pointer, need to save the left point and right pointer to local variables. Then change the root node, then recursive call left branch, right branch. Return the head. Right, which is the head of the tree node.

How about converting the tree to a double-linked list?
Need to change to 
```python
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        head = TreeNode()
        tail = head

        def preorder(node):
            nonlocal tail
            if not node:
                return
# need to save it. As in the preorder(left_branch) may change the pointer.
            left_branch = node.left
            right_branch = node.right

            tail.right = node
            node.left = tail
            tail = tail.right

            preorder(left_branch)
            preorder(right_branch)

        preorder(root)
	Head = head.right
	Head.left = None
        return head
```
### 430. Flatten a Multilevel Doubly Linked List
TIPS: the trick is processing current node, then child, then next. When processing the next node, it can be changed in the processing the children node. So, need to save next point before processing the children nodes
```python
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        new_head = Node()
        cur = new_head

        def dfs(node):
            nonlocal cur
            if node is None:
                return None
            else:
                next_node = node.next

                cur.next = node
                node.prev = cur
                cur = cur.next
                if node.child:
                    dfs(node.child)
                    node.child = None
                # this node can be changed in the child process
                dfs(next_node)

        dfs(head)
        cur.next = None
        new_head = new_head.next
        new_head.prev = None
        return new_head
```
## g.	Serialize and Deserialize Binary Tree

## h.	Maximum Depth of Binary Tree
### 102. Binary Tree Level Order Traversal
BFS or recursive function with the level parameters.

### 104. Maximum Depth of Binary Tree (Easy):
TIPS: start BFS search root node. Record the depth or pass the depth of the parameter to a recursive function.
Or DFS each node. Return max(left, right) + 1 for each node.

## i.	Same Tree
## j.	Add two Tree
### 617. Merge Two Binary Trees
## k.	Binary Tree Level Order Traversal
## l.	Encode and Decode Strings
## m.	Binary Tree view
From left, right, top or bottom.
TOP: BFS with column. If find an existing column node, ignore them.
Left: preorder or inorder
Right: root, right child, left child
Bottom: BFS search, the later node overrides the previous node
### 199. Binary Tree Right Side View
Keep the depth of the tree, set the depth as DFS parameters, root, right child then left child. The condition of adding the node to the result is if the length of the result list is greater than the depth.

### 545. Boundary of Binary Tree
Left boundary, leaves, right boundary.

## n.	Binary Tree Level
### 116. Populating Next Right Pointers in Each Node
### 117. Populating Next Right Pointers in Each Node II
The difference between 116 and 117 is that 116 is a perfect binary tree, while 117 is not.
TIPS: BFS searching for the binary tree. Put root to an empty list. start BFS with all the elements in the list. Each BFS loop needs two steps. 
The first step is assigning the node's next pointer. pop up the element of the list on the same level, the current node has the right node in the list, assign the current node's next pointer to the next node.  
The second step is to put the current node left node and right node to the end of the list. repeat the process until the list is empty.
## o.	Binary Tree column index

## p.	Graph Validate Tree
### 261. Graph Valid Tree (This is a typical undirect graph traverse question)
TIPS: find out if the graph is a tree or not. First, convert edges to graphs. Because the edges are unidirectional. Need to save both directions. The second starts from the root node. DFS searches from the root node and adds the visited node into a hash table hash set. In the next step, if see a node in the hash set, return False. Which means not a tree. In the DFS, need to loop over the neighbor nodes which are different from the previous nodes. So, need to pass the previous node, current node, visited hash table, and the map into a function.

Node in visited to check if there is a circle. Node!= Prev to make sure the dfs is propagated to the next node.

### 743. Network Delay Time (one pattern of BFS)
TIPS: it is a typical graph traverse. Keep the dict to record the delay time/cost. Convert the graph to a dict, the key is the start node, and the value is (end, time).  create a dict min_travel_dict to record the minimum travel time.
add the current node to a node_list. breath first search the current node list. In the loop, pop up the first element len(node_list) times. For each popped element, find the next node and weight. If the next node value is greater than the current node + weight or does not have such a node, then add the next node to the node_list (the difference is adding the condition when adding new nodes to the node_list). add the new value to the min_travel_dict.

What about calculating the task complete time if the graph is task dependent graph, w is the finish time. the changes required is changed the condition from “>” to “<”

### 94. Binary Tree Inorder Traversal
### 101. Symmetric Tree
### 110. Balanced Binary Tree (Easy)
### 543. Diameter of Binary Tree (Easy)
Tips: find the left child's maximum depth, right maximum depth, and maximum diameter is max(l + r +1). The return value is the maximum depth of the left child and the right child.
### 1973. Count Nodes Equal to Sum of Descendants
TIPS: similar with diameter of binary tree. Return the sum of left child right child and current nodel in DFS. 
### 1522. Diameter of N-Ary Tree
It is a variation to 543. The difference is the N-ary tree.
```python
class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0

        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            else:
                max_depth = 0
                for child in node.children:
                    depth = dfs(child)
                    diameter = max(diameter, max_depth + depth)
                    max_depth = max(max_depth, depth)
                return max_depth + 1

        dfs(root)
        return diameter
```
### 1245. Tree Diameter
TIPS: it only provides edges pairs, not the root of a tree. Convert all the edges into bidirectional graph. For each node, start DFS searching a path, find the longest path.
```python
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        G = defaultdict(list)
        for v, w in edges:
            G[v].append(w)
            G[w].append(v)
        self.maxdepth = 0
        self.maxv = None

        def dfs(v, d, visited):
            if v in visited: return
            visited.add(v)
            if self.maxdepth <= d:
                self.maxdepth = d
                self.maxv = v
            for w in G[v]:
                dfs(w, d + 1, visited)

        dfs(0, 0, set())
        self.maxdepth = 0
        dfs(self.maxv, 0, set())

        return self.maxdepth
```
### 687. Longest Univalue Path
TIPS: similar with diameter of binary tree. The difference is adding the previous node to the DFS function. Get left and right bfs function. If pre == current node value, return 1 + max(left, right). Else return 0.
```python
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        max_len = 0

        def recursive(prev, root):
            nonlocal max_len
            if not root:
                return 0
            left = recursive(root, root.left)
            right = recursive(root, root.right)
            max_len = max(max_len, right + left)

            # return the previous call.
            if prev and root.val == prev.val:
                return 1 + max(left, right)
            return 0

        recursive(None, root)
        return max_len
```
### 1026. Maximum Difference Between Node and Ancestor
TIPS: similar with 1245. Pass the path to the parameter of dfs. Calculate min and max. the difference is max(res, abs(node.val – min), abs(node.val – max)) then add current node.val to the path. Call left, right. Finally, pop the current node.val from the path.

### 1973. Count Nodes Equal to Sum of Descendants
TIPS: define dfs function return the sum of left, right branch and current node. 

### 113 Path Sum II
TIPS: the path start from the root end to any node of the tree.
```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []

        def backtracking(root, target, tmp):
            if root:
                if root.left is None and root.right is None:  # leave
                    if target == root.val:
                        tmp.append(root.val)
                        res.append(list(tmp))
                        tmp.pop(-1)
                else:
                    tmp.append(root.val)
                    if root.left:
                        backtracking(root.left, target - root.val, tmp)
                    if root.right:
                        backtracking(root.right, target - root.val, tmp)
                    tmp.pop(-1)

        backtracking(root, targetSum, [])
        return res
```
TIPS: Tree + backtracking, preorder iteration over the tree, backtracking 
Pay attention: the end condition is root.left is None and root.right is None. Because only the left and right node is None, the root is a leave, if only one child is None, the node is not a leave. 

What if any path from the root (not necessary to the leaves)?
Change the if root.left is None and root.right is None:  directly check if sum(tmp) == target

What if any path in the tree (not necessarily from the root)?
Adding backtracking (root.left, target, []): and backtracking(root.right, target,[]): at the end.

### 437. Path Sum III
TIPS: calculate the accumulative sum over the path. Similar with consecutive subarray sum to target. The difference is traverse the tree. When traverse the tree. Add the accumulative sum into a hash table. Check if current accumulative sum – target is in the hashtable or not. If in the hashtable count the number, if not, go left, and right branch, at last remove the current value from cumulative sum hash table.
Attention: because of the left subtree and right subtree not linked directly. When visited left subtree, we need to remove the left subtree, and then start the right subtree. So, if finish current node traverse. Need to remove sum_local from the dictionary. Decrease the sum_so_far at the end if put the sum_so_far to global variable. 
```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.n_path = 0

        def recurPathSum(root, sum_upto_now):
            if not root:
                return
            sum_local = sum_upto_now + root.val

            if sum_local - targetSum in sum_freq:
                self.n_path += sum_freq[sum_local - targetSum]
            if sum_local not in cumfrey:
                sum_freq[sum_local] = 1
            else:
                sum_freq[sum_local] += 1

            recurPathSum(root.left, sum_local)
            recurPathSum(root.right, sum_local)

            sum_freq[sum_local] -= 1
            if sum_freq[sum_local] == 0:
                del sum_freq[sum_local]

        sum_freq = {0: 1}
        recurPathSum(root, 0)

        return self.n_path
```
### 298. Binary Tree Longest Consecutive Sequence
The solution is not exactly the requirement
TIPS: keep the maximum length of the path including the current node. Check the left subtree length, and the right subtree length.  Return the maximum of left subtree length and right subtree length. 

A variation: if the left, cur, right branch can form a consecutive sequence. For each node, need to keep the increasing order length and decreasing length. Because we don’t know whether to use it left branch or right branch. for each node, return the maximum increasing length and maximum decreasing length.

### 101. Symmetric Tree (Easy)

### 841. Keys and Rooms
TIPS: depth-first search the room. Get the value of the room_num as room_num. 
Pay attention, starting from 0 or try every element. If try every element, need to reset visited=set() and try every room index. Then check if the visited room is equal to all room numbers. If try the first element, just need to dfs(0)

### 1110. Delete Nodes and Return Forest (Medium)
TIPS: return the current node in the dfs function, recall the left and right branches. Need to keep the original left and right subtree. If the current node is in the delete nodes, save the children's head to the result if the children are not in the delete nodes.
Requirements 1: collect the subtree after delete.
Requirements 2: need to reassign the value of left child and right child.
Pay attention: to the end condition. The end condition is None node or left child and right child are None. Need to collect all the subtrees including the remaining trees. So need to assign node.left and node.right. if deleted, retrun none, else return current node. Also need to resign the left child and right child pointer.

### 450. Delete Node in a BST
TIPS:  delete a node in BST need to change the value of the node other than delete the node.
```python
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # If the root is None, return None
        if not root:
            return None

        # If the key to be deleted is less than the root's key,
        # then the function is recursively called with the left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # If the key to be deleted is greater than the root's key,
        # then the function is recursively called with the right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # If the root has no child or only one child, then the root is replaced with its child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # If the root has two children, then the inorder successor of the root is found
            else:
                node = root.right
                while node.left:
                    node = node.left
                # The value of the inorder successor is copied to the root
                root.val = node.val
                # The inorder successor is then deleted from the right subtree of the root
                root.right = self.deleteNode(root.right, node.val)

        return root
```
### 865. Smallest Subtree with all the Deepest Nodes
TIPS: the deepest nodes common ancestor. Return depth and node. DFS returns the depth of the node. Check the left and right child, if left child is deeper than right child. Return left child return with depth + 1. If the right depth is deeper than left child, return right child return with depth + 1. If they are equal, return max (left depth, right depth) and current node.
```python
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return 0, None
            else:
                l, r = dfs(node.left), dfs(node.right)

                if l[0] < r[0]:
                    return r[0] + 1, r[1]
                elif l[0] > r[0]:
                    return l[0] + 1, l[1]
                else:
                    return max(l[0], r[0]) + 1, node

        depth, node = dfs(root)
        return node
```
### 285. Inorder Successor in BST
```python
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        self.successor = None

        def inorder(root):
            if not root:
                return False
            if root.val > p.val:  # if p.value is greater than current node, no need to search left branch
                inorder(root.left)
            # the frist node which has value greater than p, that is the first successor
            if root.val > p.val and not self.successor:
                self.successor = root

            inorder(root.right)

        inorder(root)
        return self.successor
```
TIPS: Be aware of BST. Inorder search the TREE, the node should be visited from lowest to highest. So, when find the first element > p.value, the node should be the successor. (note: because of BST, if the current node is less than the p.value, no need to search the left branch.)

## q.	BFS
### 637. Average of Levels in Binary Tree (Easy)

### 993. Cousins in Binary Tree
TIPS: BFS search the tree from (root, parent_node, level), search left and right branch. adding them to the queue. If find the two the nodes. compare the level and parent (level need to be the same, parent should be different)

### 623. Add One Row to Tree
TIPS: BFS search the tree. Add the level with the node, when reach depth -1, add the new node to the left and right branch. be careful when adding the new node to the 1 depth (before the root).

## r.	DFS
### 366. Find Leaves of Binary Tree
TIPS: DFS search the tree. And add remove one leave nodes. do while root until all nodes is removed.
```python
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def recurse(node):
            if not node:
                return None
            if not(node.left or node.right):
                res[-1].append(node.val)
                return None
            node.left = recurse(node.left)
            node.right = recurse(node.right)
            return node
        while root:
            res.append([])
            root = recurse(root)
        return res
```
### 606. Construct String from Binary Tree
TIPS: DFS searches the binary tree. Add bracket when go left or right child. Be careful, in the requirements, if right child is not none, need to add () to left branch even if left branch is empty.

### 2265. Count Nodes Equal to Average of Subtree
TIPS: define DFS function, return number of nodes and sum of the nodes. 
```python
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                return 0, 0
            else:
                l_n, l_sum = dfs(node.left)
                r_n, r_sum = dfs(node.right)

                average = (l_sum + r_sum + node.val) // (l_n + r_n + 1)
                if node.val == average:
                    res.append(node.val)

                return l_n + r_n + 1, l_sum + r_sum + node.val

        dfs(root)
        return len(res)
```

## s.	Inorder
### 105. Construct Binary Tree from Preorder and Inorder Traversal (Medium)
### 501. Find Mode in Binary Search Tree
TIPS: in order to traverse the tree (the value will be visited in nondescending order). And counting the number of the same value nodes.  Like finding the most frequent item in an array. The difference is one is an array, the other is a binary search tree.
### 515. Find the Largest Value in Each Tree Row
TIPS: BFS the tree. For each level find the max value. Save the max value to the result.
## t.	Binary Tree indexing
### 919. Complete Binary Tree Inserter
Save the tree nodes into a dictionary. The key is the index of the tree. The parent node is ind, and the left children node is 2*ind. the right children node is 2*ind + 1.
Note: 
if the node starts from 0, the left child is 2*n + 1. And the right child is 2*n + 2
If the node starts from 1, the left child is 2*n, and the right child is 2*n + 1
```python
class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.d = dict()
        def dfs(node, i):
            if not(node): return 0
            self.d[i] = node
            return 1 + dfs(node.left, 2*i) + dfs(node.right, 2*i+1)
        self.root = root
        self.l = dfs(root, 1)

    def insert(self, val: int) -> int:
        self.l += 1
        self.d[self.l] = TreeNode(val)
        if(self.l % 2):
            self.d[self.l//2].right = self.d[self.l]
        else:
            self.d[self.l//2].left = self.d[self.l]
        return self.d[self.l//2].val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
```
## u.	Preorder
### 144. Binary Tree Preorder Traversal (Medium)

## v.	Postorder
### 814. Binary Tree Pruning
TIPS: typically, a recursive function in postorder, which is left, right and current node. This is because we only process the current node if we already processed the left and right subtree. Check the left branch, check the right branch, and process the current node. Return if the current node has 1 or the left branch has 1 or the right branch has 1.
Pay attention to the return of the recursive function, and the current return are the same.

### 449. Serialize and Deserialize BST
```python
class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """

        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []

        return ' '.join(map(str, postorder(root)))

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """

        def helper(lower=float('-inf'), upper=float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None

            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root

        data = [int(x) for x in data.split(' ') if x]
        return helper()
```
first to handle the end recursive function condition, then current node processing and last is return. The end condition is the very last element that doesn’t apply to the condition. That means the node is not in the current subtree. Return None in this case.  Processing the current node, create a node with the last element value, then the right subtree, left subtree returns the current node.

What about a non-binary search tree? Only need to change to save None to in serialization, and in deserialization, if encounter None, return None instead of comparing the last element of the array.

Serialization and Deserialization order: 
If preorder in serialization, root + left child + right child, in deserialization, need to parse the list from start to the end in sequence, root, left child, right child.
If postorder in serialization, left child + right child + root. In deserialization, need to parse the list from right to left, and assign the nodes to root, right child, left child.

## w.	Binary Search Tree
### 99. Recover Binary Search Tree (Hard)
### 669. Trim a Binary Search Tree (Easy) (a pattern to change a tree)
Pay attention, this question needs to be removed from all nodes if node.value is not between low and high. Tips, return the left child root node or right child root node, 
```python
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left) # return a node in left that is follow rules
                node.right = trim(node.right) # return a node in right child that is follow rules
                return node  # always return a node. Because of node.left and node.right assignment.

        return trim(root)
```
what about keep the node if current node is not valid but left or right child is valid. the logic would be checking left child, check right child, if left_check or right_check or current_node, return True, else return False, if remove current node, need to define return trim(node.left), return(node.right)

### 95. Unique Binary Search Trees II
TIPS: the root node can be any nodes. so, iteration of from left to right. Find the root node and recursively call dfs function to generate left subtree and right subtree. The possible of left subtree and right subtree is product of return of left subtree and right subtree.
```python
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def getTreeList(nodes):
            if not nodes:
                return [None]
            res = []
            for i, val in enumerate(nodes):
                for leftTree, rightTree in product(getTreeList(nodes[:i]), getTreeList(nodes[i + 1:])):
                    res += [TreeNode(val, left=leftTree, right=rightTree)]
            return res

        return getTreeList(tuple(range(1, n + 1)))
```
## x.	Modified traverse tree
### 314. Binary Tree Vertical Order Traversal
Two solutions: BFS or DFS
Tips: add extra parameter in traverse tree function, add depth, column, row

### 339. Nested List Weight Sum, tips: passing the level to the sum function
TIPS: add level to the parameter in order to multiply the elements of the list.

### 938. Range Sum of BST
Questions: Does the BST include the same value node?

## y.	Prefix tree
For interview, brutal force solution is startswith.

### 208. Implement Trie (Prefix Tree) (Medium)
Questions: is the Trie case sensitive?

### 676. Implement Magic Dictionary
TIPS: using a tire to implement the algorithm. But the matching algorithm allows 1 letter is not mismatched. Add the mismatched letter to the parameter of dfs function.

### 648. Replace Words
TIPS: using trie to implement the algorithm. build tire with the roots. Split the string. For each word in the string, using trie to match the words. if match a root word break the matching and add the trie words to the result. 

### 1268. Search Suggestions System
TIPS: using suggestion words to build the prefix tree. And search the prefix tree. Sort the result and return the first 3 elements.

## z.	Convert nodes in a sequence of lists.
Tips: create a HashMap to save the order of the sequence
### 314. Binary Tree Vertical Order Traversal
Question: the order of vertex in the array matters. If low lever in the front. Should use BFS. If does not matter, both DFS and BFS work.
aa.	Convert tree nodes into a list in an order.
bb.	Balance a binary tree
### 1382. Balance a Binary Search Tree
TIPS: put all the values of bst into a nums, then create binary search tree from nums
### 110. Balanced Binary Tree
TIPS: return the maximum depth of the node in dfs. And compare left child depth to right child depth. If the absolute difference > 1. It is not balanced.

## cc.	Deserialize binary tree
Serialize: postorder traverse the tree 
           Left + right + [root] if root else []
Deserialize: add low and high to the function, and check if the value of last node is between the low and high value, if not (current value is not in this subtree), return None, if yes, pop the current node
node.right = help(value, high) 
node.left = help(low, value) return current node

### 226. Invert Binary Tree (Easy)
TIPS: switch the entire left and right subtree. Then switch the subtree nodes. for every node, switch left and right child tree. Then do the same to the left and right child tree. 
### 617. Merge Two Binary Trees (Easy)

### 572. Subtree of Another Tree (Easy)
TIPS: define a function same_tree. Parameters are two nodes, deal with return value if any node is None. Processing the current node, check if the node value is the same, if same value, return same_tree(left_child) or same_tree(right_child). If the current node value is not the same, return False directly.
Def DFS to check root node with subtree, check if the current subtree is the same as the subtree, is True, and returns True. Otherwise check left or right branch of the current subtree is the same as the subtree. 

What about returning the node of the big tree?


### 958. Check Completeness of a Binary Tree
BFS search the tree, once encounter a None in the queue, stop the BFS search, and all elements in the queue need to be None

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        while queue[0] is not None:
            node = queue.pop(0)
            queue.append(node.left)
            queue.append(node.right)
        return all([n is None for n in queue])


404. Sum of Left Leaves
Add left_or_right parameter to the dfs. Collect the leaf node and left_or_right == ‘L’ values.

513. Find Bottom Left Tree Value (Easy)
538. Convert BST to Greater Tree (Easy)
TIPS: DFS search the tree. Use nonlocal variable collect the sum of the tree node value. Add the value to the node value. Add the value by the total. Then add node.val to the total. Be careful to save the node.val. change the value.
1038. Binary Search Tree to Greater Sum

235. Lowest Common Ancestor of a Binary Search Tree (Easy)
TIPS: Can use the BST node feature to decide whether to check the left tree or right tree
Find the paths of two nodes and compare the two paths using DFS + backtracking.

530. Minimum Absolute Difference in BST (Easy)
TIPS: in order traverse the BST, all the elements are in order.
889. Construct Binary Tree from Preorder and Postorder Traversal (Medium)
106. Construct Binary Tree from Inorder and Postorder Traversal (Medium)

1008. Construct Binary Search Tree from Preorder Traversal
TIPS: typically, tree construct algorithm. add the lower and higher boundary to the dfs function. The difference between binary tree and binary search tree is the root value less than all nodes of right subtree. The root value is higher than all nodes of the left subtree. (need to confirm is the tree has duplicate value or not), if the tress has the duplicate value need to put None into the list. Otherwise, if has the same value as root node, it can be left or right child.
```python
1009. class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def construct(lower, higher, l):
            if not l:
                return None
            elif l[0] < lower or l[0] > higher:
                return None
            else:
                node = TreeNode(val=l.pop(0))
                node.left = construct(lower, node.val, l)
                node.right = construct(node.val, higher, l)

                return node

        root = construct(float("-inf"), float("inf"), preorder)
        return root
```

### 94. Binary Tree Inorder Traversal (Medium)
### 145. Binary Tree Postorder Traversal (Medium)

### 109. Convert Sorted List to Binary Search Tree (Medium)
TIPS: fast and slow pointers to get the middle node of the linked list, break the list with the previous node of the slow pointer, and assign the previous node of the middle node next node as None. Then split the whole problem into two subproblems, creating a binary search tree from the left half-linked list. Creating a linked list from the right half of the linked list.  Then recursively call the function until all the node is traversed.
把排好序的链表变成BST。为了使得BST 尽量平衡，我们需要寻找链表的中点。
1.	find middle pointer.
2.	assign previous of middle node next pointer to None
3.	check if head == middle, if yes, return current node. Directly. If no create left and right branch
4.	recursively call this function with head and middle pointer. Crete left branch and right branch
5.	return current node.
### 897. Increasing Order Search Tree (Easy)
Tips:
```python
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        head = TreeNode()
        cur = head
        def inorder(node):
            nonlocal cur
            if not node:
                return None
            else:
                inorder(node.left)
                # need to change current node left.
                node.left = None
                cur.right = node
                cur = cur.right
                
                inorder(node.right)

        inorder(root)

        return head.right
```
### 653. Two Sum IV - Input is a BST (Easy)
Red and black tree
### 333. Largest BST Subtree
TIPS: return the max, and min for each node. And check left subtree max, current value, right subtree min. if follow the BST. 
```python
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def postOrder(root):
            if not root:
                # min value is +inf /  max value is -inf
                # Since if null node to left then its max < root.val
                # And if null node to right then its min < root.val
                # As we set min as +inf and max as -inf this will be true
                return (math.inf, -math.inf, 0)

            leftMin, leftMax, leftNodes = postOrder(root.left)
            rightMin, rightMax, rightNodes = postOrder(root.right)
            # For a parent to be BST its left trees max should be less
            # And its right trees min should be greater
            # Post order we visit child first then parent
            # So we first visit smaller BST then larger.
            if leftMax < root.val < rightMin:
                # We want to know max and min value of all nodes
                # rooted at this root.
                maxVal = max(leftMax, rightMax, root.val)
                minVal = min(leftMin, rightMin, root.val)
                return (minVal, maxVal, leftNodes + rightNodes + 1)
            else:
                # As not a BST we want BST check to fail for all nodes above this node.
                # So min is -inf and max is +inf
                # If left - parent will check max < root.val and fail
                # If right - parent will check root.val < min and fail
                # Bubble up the maxNode from left and right as they can have ans
                return (-math.inf, math.inf, max(leftNodes, rightNodes))

        minVal, maxVal, nodes = postOrder(root)
        return nodes
```

### 894. All Possible Full Binary Trees
TIPS: find if postorder, inorder or preporder, the key is the logic of return, if need to find out left child and right child, need postorder, if need find the current node, then calculate the left child or right child, need preorder. If need check left child, root then right child, need inorder. The key is the logic to get the return value.
```python
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 1:
            return [TreeNode()]

        result = []
	# every left branch has 1, 3, 5 nodes. so iteration from 1 to n-1, step is 2
	# or for left, right in product(self.allPossibleFBT(k), self.allPossibleFBT(n-1-k)).
        for k in range(1, n - 1, 2):
            for left in self.allPossibleFBT(k):
                for right in self.allPossibleFBT(n - 1 - k):
                    result.append(TreeNode(0, left, right))

        return result
```

### 530. Minimum Absolute Difference in BST
TIPS: inorder search the binary search tree. The minimum difference is between the nodes traversed by inorder sequence. So define prev to record the previous node, and calculate the difference of current node previous node. Find the minimum value.

### 337. House Robber III
TIPS: DFS return the sum with root, and sum without root.
```python

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return [0, 0]
            leftpair, rightpair = dfs(root.left), dfs(root.right)
            withroot, without = root.val + leftpair[1] + rightpair[1], max(leftpair) + max(rightpair)
            return [withroot, without]

        return max(dfs(root))
```
### 110. Balanced Binary Tree
TIPS: balanced tree definition: every node left child height and right child height difference is less than 1.define a dfs function of return the height of the subtree. Define a global variable balanced with True, if abs(left_child_height – right_child_height) > 1, balance = False. 

### 310. Minimum Height Trees
TIPS: similar with 210 topological paths. BFS from leaves until the root.
```python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        total_node_count = n

        if total_node_count == 1:
            # Quick response for one node tree
            return [0]

        # build adjacency matrix
        adj_matrix = defaultdict(set)

        for src_node, dst_node in edges:
            adj_matrix[src_node].add(dst_node)
            adj_matrix[dst_node].add(src_node)

        # get leaves node whose degree is 1
        leave_nodes = [node for node in adj_matrix if len(adj_matrix[node]) == 1]

        # keep doing leave nodes removal until total node count is smaller or equal to 2
        while total_node_count > 2:

            total_node_count -= len(leave_nodes)
            leave_nodes_next_round = []
            # leave nodes removal
            for leaf in leave_nodes:

                neighbor = adj_matrix[leaf].pop()
                adj_matrix[neighbor].remove(leaf)
                if len(adj_matrix[neighbor]) == 1:
                    leave_nodes_next_round.append(neighbor)
            leave_nodes = leave_nodes_next_round
        # final leave nodes are root node of minimum height trees
        return leave_nodes
```