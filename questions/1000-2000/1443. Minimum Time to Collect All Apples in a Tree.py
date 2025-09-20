
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # define DFS function
        def dfs(node):
            visited.add(node)
            ct = 0
            for nxt_node in graph[node]:
                if nxt_node not in visited:
                    steps = dfs(nxt_node)
                    if steps != -1:
                        ct += 2
                        ct += steps
            if hasApple[node] or ct > 0:
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