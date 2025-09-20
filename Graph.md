# Graph
1.	# Backtracking algorithm, BFS or DFS or a combination of those algorithms
2.	# Typically convert the graph to bidirectional hash table, then we can use BFS or DFS to search if the neighbour is implicit. 
3.	The condition of BFS or DFS may vary.
4.	# The difficulty is how to convert existing problems to directional or unidirectional graphs. Then BFS or DFS searches the graph.
5.	# Typical question. Gradually put the edges into graph, before adding current edged into graph, check if nodes are connected without current edge. Similar operation is putting list element into dictionary.
6.	Build the connection in a loop, and add process during adding the connections
7.	Build bidirectional graph, remove connection in a loop, and check the connection importance.
8.	1192 explore the essence of DFS and Graph. If understand the solution, the essence of DFS and graph are fully understood
9.	Tree diameter: if it is tree organized with graph data structure, check maximum depth of left subtree and right subtree. The diameter is the maximum depth of left subtree and right subtree. If it is organized by edge connection, need to connect edges into graph, find the maximum depth of tree, from the node of the maximum depth, search the maximum depth of the tree. If does not know the root node, need to iteration every node and find the maximum depth. Attention in the DFS, need to add previous node and current node, when looking for the neighbours, ignore the previous node.
10.	Connecting nodes in a graph with lowest cost. Converting the connections between each node into a graph. BFS search from starting of the node and put the connection cost to each new nodes into a Heap until all the nodes are popped from the heap.
11.	Visited is a dictionary, the key is the node, the value is the depth of the node, for example 1761

## a.	Normal calculation
### 296. Best Meeting Point: (similar with 1135. Minimum cost to connect all cities)
Tips: inverse thinking, find out all the cells to the 1s cell. Start from all 1 cell, searching surrounding cell, keep the distance to the 1 cell.
Find all 1s points. BFS overall grid and find all the distances to the current cell for all other cells. Then we get the point to all the 1s. sum all the distance and get the best position which reaches all 1s lowest distance.
The distance hash table is organized like dis_hash[position] = [distance1, distance2, distance3], so it is easier to add them up.

Two ways of calculation, from other cells to destination or from destination to another cell. In this case, from the destination to other cells is better. 

## b.	Number of all possible route
Calculate the total number of possible routes.

## c.	Print all possible routes (meta. RRDD)
TIPS: the same with print all possible routes, backtracking and DFS, when reaching the destination print out the route or deep copy the route (because backtracking will change the memo).

### 797. All Paths from Source to Target
TIPS: create a DAG graph from edges. And do DFS from 0 to target. If find one path, put it in the result. Be careful of the starting node.

## d.	Topological sort. ******
### 210. Course Schedule II (Medium)
TIPS: define indgree list (each), dependency dict and res (prerequisite course is the key, dependent course is the value). DFS search node if indegree is 0. For each node, add the node to the result, then iterate over the courses depended on such courses which indegree is 0.

## e.	minimum spanning tree question
### 1584. Min Cost to Connect All Points
Typical solution for minimum cost to connect points
TIPS: the principle is how to find the lowest distance between two group points. Imagine we have two group points, we gradually put the points from left to right one by one. But we only picked the nearest point to the new set of points. 
Steps: get each point distance to others. And create a tuple (distance, point_ind). First, pick one point to the right. And put the pint into the visited table. Then we look for the next point to the right. We happify the distance tuple of the point. Pop the first element (imagine putting the element to the right) and find all the distance tuples into the heap.  The heap will include all the points and distances from the selected two points. The first element of the heap is the lowest distance point to the group.

## f.	Graph + BFS
### 2092. Find All People with Secret
Building the graph by the time.
TIPS: sorting the array and grouping the array with the key to time.  Need sorting is because of the need to iterate from low to high, need to group by the time, need to operate at the same time.  Build the graph a single time. Then BFS searches the graph if one of them knows the secret.
At one time, create the graph, DFS search the graph. At the other time. Do it again.
from collections import deque, defaultdict
from itertools import groupby
```python
class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        can = {0, firstPerson}
        for _, grp in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            queue = set()
            graph = defaultdict(list)
            for x, y, _ in grp:
                graph[x].append(y)
                graph[y].append(x)
                if x in can: queue.add(x)
                if y in can: queue.add(y)

            queue = deque(queue)
            while queue:
                x = queue.popleft()
                for y in graph[x]:
                    if y not in can:
                        can.add(y)
                        queue.append(y)
        return can
```
## g.	Tarjan's

### 1192. Critical Connections in a Network
Wonderful, the DFS typical workflow
```python
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(list)
        for node1, node2 in connections:
            graph[node1].append(node2), graph[node2].append(node1)

        arrival_time = [None] * n
        critical_connections = []

        def dfs(node=0, parent=-1, time=1):
            # First section, call DFS and assign the value of arrival time
            if arrival_time[node]: return  # only keep the original arrival time.
            arrival_time[node] = time
            for neighbour in graph[node]:
                if neighbour == parent: continue
                dfs(neighbour, node, time + 1)
                # the second section
#all the linked neighboour arrvial time assigned, from the deepest arrival time, check belows
                if arrival_time[neighbour] == time + 1:
                    # when before entering the DFS, it is empty, but call neighour, not encounter a loop in neighbour nodes and all the nodes connecting to neighbour
                    critical_connections.append((node, neighbour))
                else:
                    # if find a loop, It is due to DFS feature, the first loop node is the previous visited node.
                    # all the loop depth will be assigned the same depth which is the first node of loop
                    arrival_time[node] = min(arrival_time[node], arrival_time[neighbour])

        dfs()
        return critical_connections
```
Alternative: convert all edges to directional graph, iteration each edge, remove the connection from the graph, try to find a path from source to target, if yes, current edge is not critical, if not, current edge is critical.

## h.	Shortest path
### 787. Cheapest Flights Within K Stops
TIPS: Graph + DFS or BFS
DFS version
```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        m = len(flights)
        for i in range(m):
            u, v, w = flights[i]
            adj[u].append((v, w))

        @lru_cache(None)
        def dp(u, k):
            if u == dst: return 0
            if k == 0: return math.inf
            ans = math.inf
            for v, w in adj[u]:
                ans = min(ans, w+dp(v, k-1))
            return ans

        ans = dp(src, k+1)
        return ans if ans != math.inf else -1
```
BFS version
Cost array keeps the lowest cost of each stop.  Iteration K times other than while loop.
```python

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for s,e,p in flights:
            graph[s][e] = p
        cost = [math.inf for _ in range(n)]
        q = deque([[src, 0]])
        for _ in range(k+1):
            size = len(q)
            for _ in range(size):
                [ele, curCost] = q.popleft()
                for nextNode in graph[ele]:
                    nextNodePrice = curCost+graph[ele][nextNode]
                    if nextNodePrice<cost[nextNode]:
                        cost[nextNode] = nextNodePrice
                        q.append([nextNode, nextNodePrice])
        if cost[dst]==math.inf:
            return -1
        return cost[dst]
```
### 834. Sum of Distances in Tree
TIPS: convert the tree to a graph. For one node. DFS searches all the graph nodes and returns the distance to the nodes.  pay attention to not searching the previous node again (put the previous node to the parameter of the DFS function and add the condition to find the next node).  Add the distance to the parameter of DFS function.
BFS version. Convert all nodes to graph. Loop every node, BFS the start node, keep record the distance. When encountering a node add the distance to the total distance of current node.

### 847. Shortest Path Visiting All Nodes
TIPS: the keys are the nodes that can be visited multiple times. Using the last visited node + path (mask) to find if the node is visited or not.
```python

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque()
        # [n_nodes, mask] to save visited nodes. power(2, n) 
        visited = [[False] * (1 << n) for _ in range(n)]

        # generate multiple channel of BFS
        for i in range(n):
            queue.append((1 << i, i, 0))
            visited[i][1 << i] = True

        while queue:
            mask, x, dist = queue.popleft()

            # visited all nodes. the first one is the shortest path
            if mask == (1 << n) - 1:
                return dist

            # checking the neighbour
            for neighbor in graph[x]:
                # adding current node to the path (or )
                new_mask = mask | (1 << neighbor)
                # if visited nodes are the same (new_mask) and reach the same node (neighbor)
                # ignore it. because it is longer than the previous one.
                if not visited[neighbor][new_mask]:
                    queue.append((new_mask, neighbor, dist + 1))
                    visited[neighbor][new_mask] = True
```
### 684. Redundant Connection
TIPS: do not create all edged to graph at the beginning. Iteration from left of the edges. Create the graph in the iteration, gradually add edges to the graph. Before adding the edges to the graph, check if there is a path between two edges, if yes, return the edge.
```python
class Solution:
    def findRedundantConnection(self, edges):
        # variable to keep track of graph constructed so far
        graph_so_far = collections.defaultdict(lambda: [])

        # dfs function to check if path exists between nodes u and v
        def path_exists(u, v):
            # we reached to v from u
            if u == v:
                return True
            # mark u as visited
            visited.add(u)

            # iterate through all the neighbors of u and if they are not visited call dfs on them
            for neighbor in graph_so_far[u]:
                if neighbor not in visited:
                    if path_exists(neighbor, v):
                        return True

            return False

        # iterate through all the pairs of edges
        for u, v in edges:
            # we make a fresh visited because we call dfs for every pair of edges
            visited = set()
            # if path exists between u and v return that's the answer
            if path_exists(u, v):
                return [u, v]
            else:
                # if path does not exist we add edges to graph
                graph_so_far[u].append(v)
                graph_so_far[v].append(u)

        return None
```
### 133. Clone Graph: https://leetcode.com/problems/clone-graph/
Tips: make a hash table to map from the original graph vertex to the clone vertex
### 200. Number of Islands: https://leetcode.com/problems/number-of-islands/
Question: Can we change the original table? If yes, we can modify the original table, otherwise, we need to use a hash table to record the visited elements.
Tips: if find 1, the number of islands plus 1. DFS searches all cells connected to the current cell and assigns 0 to them. Or put the visited cells in a hash table
### 207. Course Schedule: https://leetcode.com/problems/course-schedule/
Tips, BFS from all course requisites. Keep a record of all visited nodes. If encounter a visited node, it has a loop. Or start from no requisites course, remove conditions which have no requisites course. and then find no requisites course until no requisites course. Check if 
### 1059. All Paths from Source Lead to Destination (Medium)
Typical DFS question. DFS to check if every route to reach the destination is in the loop, first to check the next nodes, if next node is empty and current node != destination, return False.
If current node == target, return True. 
```python

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])

        def dfs(node: int, graph: dict, visited: List[int], dest: int) -> bool:
            if len(graph[node]) == 0 and node != dest:
                return False

            for nei in graph[node]:
                if nei in visited:
                    return False
                visited.add(nei)  # need to add current node to visited before call itself.
                if not dfs(nei, graph, visited, dest):
                    return False
                visited.remove(nei)

            return True

        return dfs(source, graph, set(), destination)
```
variations: check if the graph has loop. 

### 1135. Connecting Cities with Minimum Cost (Medium)
TIPS: like 1584. Min Cost to Connect All Points
### 882. Reachable Nodes in Subdivided Graph (Hard)

### 1761. Minimum Degree of a Connected Trio in a Graph
TIPS: visited dictionary save node and node level (the depth of the node)
Question: do we need to consider the one node is shared nodes in more than one Trico? if No, DFS will work, if there are multiple Trico connecting to one node, need to be BFS.
```python
class Solution:
    def minTrioDegree(self, n: int, edges) -> int:
        # convert all edge into graph

        graph = defaultdict(list)
        trio = []

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        degree = 0

        def dfs(node, n):
            nonlocal visited
            nonlocal degree
            if node in graph:
                for nextnode in graph[node]:
                    if nextnode not in visited:
                        visited[nextnode] = n + 1
                        dfs(nextnode, n + 1)
                    else:
                        if visited[nextnode] == n - 2:
                            # find a trio
                            if (node, nextnode) not in trio and (nextnode, node) not in trio:
                                trio.append((node, nextnode))
                                degree += len(graph[nextnode]) - 2
                                dfs(nextnode, n + 1) 
					

        # add steps in the visited
        for nod in graph:
            # the value is the step number to visit the node
            visited = {}
            dfs(nod, 0)

        return degree
```
Another version: add previous node, current node in the DFS. When the previous node in the neighbor of current node's neighbor, we could find a Trico. then calculate the degree of the previous node, current node and the neighbor node degree.

### 1367. Linked List in Binary Tree
TIPS: BFS search the head node, If find a head is the same with linked list head, DFS search the linked list and the tree node.
