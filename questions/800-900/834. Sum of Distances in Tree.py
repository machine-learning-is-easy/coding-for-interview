

# treat tree as graph
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # graph

        graph = collections.defaultdict(list)
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        res = []

        @cache
        def dfs(node, pre_node, current_distance):
            nonlocal graph
            if node in graph:
                distance = 0
                for nxt_node in graph[node]:
                    if nxt_node != pre_node:
                        distance += current_distance
                        distance += dfs(nxt_node, node, current_distance + 1)
                return distance
            else:
                return 0

        for node in range(n):
            res.append(dfs(node, None, 1))
        return res