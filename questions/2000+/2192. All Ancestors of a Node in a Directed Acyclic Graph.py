
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        # Store the ancestors for each node
        ancestors = [set() for _ in range(n)]

        def dfs(src, current):
            for neighbor in graph[src]:
                if current not in ancestors[neighbor]:
                    ancestors[neighbor].add(current)
                    ancestors[neighbor].update(ancestors[current])
                    dfs(neighbor, current)

        for i in range(n):
            dfs(i, i)

        # Convert sets to sorted lists
        return [sorted(list(s)) for s in ancestors]


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree = [0] * n

        # Step 1: Build graph and in-degree count
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        # Step 2: Initialize ancestor sets and queue with 0 in-degree nodes
        ancestors = [set() for _ in range(n)]
        queue = deque([i for i in range(n) if in_degree[i] == 0])

        # Step 3: Topological Sort with ancestor propagation
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                # Add current node and all its ancestors to the neighbor
                ancestors[neighbor].add(node)
                ancestors[neighbor].update(ancestors[node])

                # Decrease in-degree and add to queue if 0
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Convert sets to sorted lists
        return [sorted(list(a)) for a in ancestors]