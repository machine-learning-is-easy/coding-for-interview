


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
                # ignore it. because it is longer than previous.
                if not visited[neighbor][new_mask]:
                    queue.append((new_mask, neighbor, dist + 1))
                    visited[neighbor][new_mask] = True


graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]

assert Solution().shortestPathLength(graph) == 4