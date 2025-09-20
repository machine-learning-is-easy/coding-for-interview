
from collections import defaultdict
class Solution:
    def treeDiameter(self, edges) -> int:

        edges_dict = defaultdict(list)
        max_diam = 0
        for start, end in edges:
            edges_dict[start].append(end)
            edges_dict[end].append(start)

        def dfs(pre_node, cur_node, step):
            nonlocal max_diam
            if cur_node in visited:
                return

            max_diam = max(max_diam, step)
            visited.add(cur_node)

            for next_node in edges_dict[cur_node]:
                if next_node != pre_node:
                    dfs(cur_node, next_node, step + 1)

        for node in range(len(edges_dict)):
            visited = set()
            dfs(None, node, 0)

        return max_diam

# another version
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

assert Solution().treeDiameter([[0,1],[0,2]]) == 2


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = {i: [] for i in range(n)}

        # Build the graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Function to perform BFS and return the farthest node and its distance
        def bfs(start):
            visited = [-1] * n
            visited[start] = 0
            queue = deque([start])
            farthest_node = start
            max_distance = 0

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if visited[neighbor] == -1:  # Unvisited
                        visited[neighbor] = visited[node] + 1
                        queue.append(neighbor)
                        if visited[neighbor] > max_distance:
                            max_distance = visited[neighbor]
                            farthest_node = neighbor
            return farthest_node, max_distance

        # First BFS to find one endpoint of the diameter
        farthest_node_from_start, _ = bfs(0)

        # Second BFS from the farthest node to find the diameter
        _, diameter = bfs(farthest_node_from_start)

        return diameter