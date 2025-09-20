
class Solution:
    def magnificentSets(self, n, edges):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        # Store max group size for each component
        comp_max = defaultdict(int)

        for start in range(n):
            q = deque([start])
            dist = [0] * n
            dist[start] = max_depth = 1
            root = start

            # BFS to calculate group sizes and check validity
            while q:
                node = q.popleft()
                root = min(root, node)

                for nei in adj[node]:
                    if dist[nei] == 0:
                        dist[nei] = dist[node] + 1
                        max_depth = max(max_depth, dist[nei])
                        q.append(nei)
                    elif abs(dist[nei] - dist[node]) != 1:
                        return -1  # Invalid group (difference not ±1)

            # Update the max group size for this component
            comp_max[root] = max(comp_max[root], max_depth)

        # Return the sum of all max group sizes
        return sum(comp_max.values())