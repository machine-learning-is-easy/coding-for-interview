# BFS
Key Points: Normally it applies to shortest path
### 1.	Initialization of a queue
### 2.	While the queue until the queue is empty
### 3.	If need to count the step, a for loop is required to pop all the elements of the queue. If not need to count the step, there is no need for a loop
### 4.	Visited set, add the element to the visited set when adding the element to the queue. Also, the visited can be a dictionary in which the keys have values, it works to 785. Is Graph Bipartite? Add to the visited set when checking the surrounding cells.
Find the shortest path needed to add the visited set. It will remove the long path (steps or later added nodes can be ignored). Because the cell can be reached earlier within the shortest path than the long path. However, the visited set cannot used in finding a weighted path which means more steps do not mean cost more.
If the element has duplicate value, need use a list to check if every element is used or not.
Visited set can be a separate variable or multiple visited set that need to be stored in the queue element.
The difference of visit set between BFS and DFS is BFS visited set collect all path visited while the DFS visited set only collect the visited node for a single path
### 5.	The queue. Need to add elements to the queue, the element of the queue can be a number, a node, a two elements tuple or three elements tuple, or the entire path. The queue can be a heap, the heap will sort the minimum element to the Front. It works to find the minimum route cost. 691. 691. Stickers to Spell Word is an example of using heap to the queue.
### 6.	Return, in the loop of adding an element to the queue, if the end condition applies, return immediately, for example, 691.
### 7.	The queue together with Heapq. When adding a new element to the queue, sort the queue with min of element of Heapq. Like 691. Often to calculate the minimum path cost.
### 8.	Topological sort.   Like 269 Alien Dictionary and 210 Course Schedule
### 9.	Open the lock. Need to create the neighbours from digits
### 10.	BFS + dict. The dict save the temp value of each node. BFS search, if find a node value less than the dict key value, put the element into the queue. Commonly for calculating min cost
### 11.	Attention when add the element into the visited set, adding the element into the visited set when adding to the stack or adding the element into the visited set when pop the element out of the stack. 
### 12.	Searching from multiple points like 994
### 13.	Two option to check the result, when pop from the queue and when adding to the queue,
If searching the minimum, check the result when pop the queue (heap).
### 14.	Disjoint union set. 
	
BFS visited set is all searching direction visited path while DFS visited set is for path by path.
Pay attention, to the variable convention, when adding the node to the visited set. We can put the element into the visited set when pop the element from the stack and add the element to visited when add the element to the stack.
A typical of BFS is 
```python
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes. Name convention is very important
queue = []   # Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:

   Step += 1
For _ in range(len(queue)): 
# Pay attention of this for loop. 
# This loop cannot be `for ele in queue`. Because ele will get the extral element after adding more element in the loop.
      s = queue.pop(0) # if need to get steps, need a loop to pop all elements
           print (s, end = " ") 

      for neighbour in graph[s]:
        if neighbour not in visited:
	# Can add an addition to add the current element to the queue and visited.
	# For example, revisited current element if the current element has a lower or higher value than the visited 
          visited.append(neighbour) # when adding to the queue, add it to the visited as well.
          queue.append(neighbour) # The queue can be a heap, the element can be a tuple.

# Driver Code
bfs(visited, graph, 'A')
```
### 934. Shortest Bridge (Medium)
Tips: DFS + BFS. Find the first 1 and DFS, and change the first island to 2, in the meantime, need to save the first 0s in the DFS. Using BFS/BFS, spread from the 0s list to the other island step by step, when encountering 1 return the steps.  
variations: 
#### 1. Blocks in the matrix. typical BFS question (it works if add any block in the matrix, it can spread from any direction, it is different from questions like start from top left to bottom right, only move right or down). 
#### 2 multiple islands, find the shortest bridge. Search all element, if find no visited 1s, bfs collect all 1s, then BFS search all possible cells and save the shortest path to the element. When complete all element, the distance to all island should be collected. And sum them up.
```python
class Solution:
    def shortestBridge(self, grid) -> int:
        def dfs(x, y):
            grid[x][y] = 2
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 1:
                        dfs(nx, ny)
                    elif grid[nx][ny] == 0: # add the first seen 0 in to a list.
                        q.add((nx, ny))

        m, n = len(grid), len(grid[0])
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = set()

        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                dfs(i, j)  # paint one island to 2, border 0 add to q
                break

        # breath first search the first seen 0s
        step = 0
        q = deque(q)
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1: return step + 1
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2  # mark visited
                            q.append((nx, ny))
            step += 1

        return step
```

### 17. Letter Combinations of a Phone Number: 

### 827. Making A Large Island

### 126. Word Ladder II (Hard) 
### 127. Word Ladder
126, 127 are similar. The difference is 126 needs to return the route, while 127 needs to return the minimum steps.  If need to return the route, DFS is better (with backtracking). if need to return the minimum steps, BFS is better.
The first step is creating the transfer graph, for a given word, remove one letter and replace the letter with `*` as the key, the value is a list, put the current word to the list.
Once the graph is created, DFS, or BFS starts with start words, removes one letter, for each transformation, finds the keys in the transformation graph, iteration over each token of the value in the transformation graph values.
No need visited. Check if the current word is in the sequence to check if already visit the word

### 691. Stickers to Spell Word: (BFS + heap)
Tips: 
Processing the sticker, convert all the stickers to a hash table, the key is the letter, and the value of the keys are list of words including the key letter.
BFS. The element in the queue is (used_sticker_num, len(residual_string), residual_string). pop the first element of the target and get all the tickers including the character. Iteration over the next possible stickers, step + 1, 
```python
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        """
        ["with","example","science"]

        "thehat"

        """
        N = len(target)
        letdic = defaultdict(list)
        tset = set(target)

        for stick in stickers:
            ls = [l for l in stick if l in tset]
            for l in ls:
                letdic[l].append(ls)

        q = [(0, len(target), list(target))]

        while q:
            used, lent, targ = heapq.heappop(q)

            if targ[0] not in letdic.keys(): return -1

            for wrd in letdic[targ[0]]:
                newtarg = targ[:]
                for lw in wrd:
                    if lw in newtarg:
                        newtarg.remove(lw)
                if not newtarg:
                    return used + 1
                heapq.heappush(q, (used + 1, len(newtarg), newtarg))

        return -1
```

### 737. Sentence Similarity II
TIPS: convert the similar words into a bidirectional graph and convert two sentences into two sets (if not consider duplicate words). Find one word from one sentence and DFS call with the word as the parameter, in DFS, if a word is in the searched sentence, remove the token from the sentence set and return true. If not search all similar words in the graph. If anyone returns the true, return True directly. 
```python

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        graph = defaultdict(list)

        for start, end in similarPairs:
            graph[start].append(end)
            graph[end].append(start)

        sentence1 = set(sentence1)
        sentence2 = set(sentence2)

        def dfs(token):
            if token in sentence1:
                sentence1.remove(token)
                return True
            elif token in graph:
                for nexttoken in graph[token]:
                    if nexttoken not in visited:
                        visited.add(nexttoken)
                        if dfs(nexttoken):
                            return True

            return False

        for token in sentence2:
            if token in sentence1:
                sentence1.remove(token)
            else:
                visited = set()
                find_similar = dfs(token)
                if not find_similar:
                    return False

        return len(sentence1) == 0
```
What about the sentence that has duplicate words, just need to convert sentences into a dictionary, the key is the word, and the value is the count of the words, in DFS, if find the word in the sentence dict, decrease the count, if the count is 0, remove the key from the dictionary.
Sentence1.remove(token) only remove token once. Not remove all tokens which is the same with token. So above solution works for multiple tokens.

### 1091. Shortest Path in Binary Matrix
```python
class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        # breath first search
        if not grid:
            return -1
        r = len(grid)
        c = len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        visited = set()
        starts = [(0, 0)]
        adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
        steps = 1
        if (r - 1, c - 1) in starts:
            return steps
        while starts:
            steps += 1
            for _ in range(len(starts)):
                cell = starts.pop(0) # has to pop 0 index
                # travers the points at the starts
                for adj in adjacent:
                    i = cell[0] + adj[0]
                    j = cell[1] + adj[1]
                    if (i, j) == (r - 1, c - 1):
                        return steps
                    else:
                        if i >= 0 and i < r and j >= 0 and j < c:
                            if grid[i][j] == 0:
                                if (i, j) not in visited:
                                    visited.add((i, j))
                                    starts.append((i, j))
        if (r - 1, c - 1) not in visited:
            return -1
        return steps
```

### 752. Open the Lock
TIPS: create the neighbours when switching one digit up or down. Do the BFS searching until reach the target. Pay attention and ignore the path which reaches deadends. It is similar to the path in 2D map with block.
```python

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i + 1:]

        queue = ["0000"]

        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0

        visited = set("0000")
        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                cur = queue.pop(0)
                for nei in neighbors(cur):
                    if nei in deadends or nei in visited:
                        continue
                    elif nei == target:
                        return step
                    else:
                        visited.add(nei)
                        queue.append(nei)

        return -1
```
### 1926. Nearest Exit from Entrance in Maze
TIPS: add the entrance to the queue. Pop all the elements from the queue. For each element, searching surroundings. Can use visited or change the maze value for recording visited element.

### 1216. Valid Palindrome III
```python
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # queue holds a tuple of `l` and `r`, and the depth `curr_k`.
        queue = deque([(0, len(s) - 1, 0)])
        visited = set()

        while queue:
            l, r, curr_k = queue.popleft()

            # If the budget is exceeded return False
            if curr_k > k:
                return False

            # Shave off the two ends of s[l:r+1] until end characters
            # don't match. Each graph node is defined by (l,r)
            # where s[l] != s[r].
            while s[l] == s[r]:
                l += 1
                r -= 1
                # if you reach the end node, you've found a k-palindrome
                if l >= r:
                    return True

            # append the two new nodes to the queue.
            if (l + 1, r) not in visited:
                queue.append((l + 1, r, curr_k + 1))
                visited.add((l + 1, r))

            if (l, r - 1) not in visited:
                queue.append((l, r - 1, curr_k + 1))
                visited.add((l, r - 1))
```
Exercises
### 130. Surrounded Regions (Medium)
TIPS: searching from four edge to find all the 0 does not surrounding by X and put them into a variable edge0, then find all 0 not in the edge0

### 839. Similar String Groups (PATTERN OF GROUP nodes)
A variation of type BFS. Not necessary to set up a visited set. Need the list of original lists of string pop up the element, so when iteration over the list will not check the element already checked. This strategy works for group elements. The key is how to check two string is similar. And create graph on similar strings. BFS or DFS in search the graph.
```python
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def checkSimilar(ref, test):
            diff = []
            for i in range(len(ref)):
                if ref[i] != test[i]:
                    diff.append(i)
                    if len(diff) > 2:
                        return False
            if len(diff) == 2:
                test[diff[0]], test[diff[1]] = test[diff[1]], test[diff[0]]
            return test == ref

        def bfs(same_group):

            for ref in same_group:  
                # we continue expand same_group size until none of string 
	       # in self.strs is similar to strings in 
                # same_groups, when same group size changes, 
                # ref continue to get the extra element.
                idx = 0
                while idx < len(self.strs): 
                    # this need to check if idx < len(self.strs), self.strs length is changing
                    if ref == self.strs[idx] or checkSimilar(list(ref), list(self.strs[idx])):  
		# same or similar
                        same_group.append(self.strs.pop(idx))
                        # self.strs size changes and same_group size changes as well
                        # the idx should not increase
                    else:
                        idx += 1
            return same_group

        self.strs = strs[:]
        groups = list()
        while self.strs:  
# continue searching similar until all string are clustered, until empty list
            groups.append(bfs([self.strs.pop()]))

        return len(groups)
```
Pay attention:
For _ in range(len(arr)) vs for elemt in arr are different. 
If arr is changed in the loop, the first will not loop the extra element index, but the second loop will get extra arr element.

### 864. Shortest Path to Get All Keys (an extension of BFS) (Also can add path in keys)
TIPs: Normally DFS to get the possible path, BFS to get shortest steps, but this question is to get the shortest path to get all keys. Need to use BFS and add path to the queue. 
This is a variation of BFS. Visited hash table element is (x, y, keys). 
First find the start point and lock number. BFS queue starts with the start point. Add (start_x, start_y, key) to queue. In the loop of BFS, pop the element, if key length equal to the length of lock, return True. If not, find neighbors, if the neighbors x, and y are valid and not a block, if current cell is a lock, check if has the key, if has the key, add (x, y, key) to the queue. If does not have the key, continue to the next cell. Check if the current cell has a key, if yes, add the key to the keys. 
Check if (x, y, new_keys) in visited, if no, add (x, y, new_keys) to the visited, and put (x, y, new_keys) to the queue. 

Attention, this solution adds a parameter in (x, y)

### 785. Is Graph Bipartite? (Medium) (Pattern of partition nodes)
This is a variation of the breadth first search by adding value to the visited set.
TIPS: breadth-first search. The variation is the condition of adding a looping queue and each node value. Assign adjacent nodes different from 1 or 0.  When checking node1 neighbours, all neighbor's values should be different to the current node (0 or 1) ^ 1. If find a neighbor which is the same as the current node, then return false. if not continue to add neighbor nodes to a dict. 
```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        hashmap = {} 
# we need to add value to the key, so it is a dict. normally, if only record visited hash table,
        # we can use set instead of dict.
        for node in range(len(graph)):
            if node not in hashmap:
                stack = [node]
                hashmap[node] = 0  
# works, because it is fully connect to other connection nodes except itself.
                # if the given graph is not fully connected with other nodes or undirectly connected. we should convert
                # it to bidirectionaly graph
                while stack: # breath first search
                    node = stack.pop()
			# does not care about steps,
                    for nei in graph[node]:
                        if nei not in hashmap:
                            stack.append(nei)
                            hashmap[nei] = hashmap[node] ^ 1 # 0 to 1 or 1 to 0
                        elif hashmap[nei] == hashmap[node]:
                            return False
        return True
```
What about returning the two groups? add a process to split the HashMap into two groups by the value of HashMap.
The difference between Reachable and steps BFS is Reachable just need to pop every component in the queue, but steps BFS, need pop all the elements in one step.

### 721. Accounts Merge
Create a graph of emails, and DFS searches on the graph to find the names and unique emails.

### 378. Kth Smallest Element in a Sorted Matrix
Starting from the top left cell. BFS the right and down direction. add the new element to a maximum heap. if the length of the heap is k and the current cell 
value is greater than the first element of the heap stops the direction search

### 407. Trapping Rainwater II
TIPS: BFS + heap. Searching from edges. Put edges into a heap. Pop heap and do BFS. Keep the level = max(height, level). If encounter a height < level. That is the amount of water trapped.
```python
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        # Initial
        # Board cells cannot trap the water
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        # Add Board cells first
        heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1

            # Start from level 0
        level, res = 0, 0

        while heap:
            height, x, y = heapq.heappop(heap)
            level = max(height, level)# the maximum of the minimum

            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n and heightMap[i][j] != -1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))

                    # If cell's height smaller than the level, then it can trap the rain water
                    if heightMap[i][j] < level:
                        res += level - heightMap[i][j]

                    # Set the height to -1 if the cell is visited
                    heightMap[i][j] = -1

        return res
```
### 2597. The Number of Beautiful Subsets
TIPS: BFS the ([], -1). And search for all next elements of the array. If the element difference is not equal to k, add to the list.
```python
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        q = deque([([], -1)])
        res = 0

        while q:
            cur, idx = q.popleft()
            res += 1

            for i in range(idx + 1, len(nums)):
                if nums[i] - k in cur or nums[i] + k in cur:
                    continue
                q.append((cur + [nums[i]], i))

        return res - 1
```
### 994. Rotting Oranges
TIPS: put all rotten oranges (i, j, time) into a queue, in the BFS pop all the elemments from the queue, searching for all neighbours, if fresh orange, change it to rotten orange, and put (I, j, time + 1) to the queue. Record the maximum time, until the queue is empty.
