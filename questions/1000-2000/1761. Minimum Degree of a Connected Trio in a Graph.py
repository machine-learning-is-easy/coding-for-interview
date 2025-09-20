

from collections import defaultdict
from heapq import heapify, heappop, heappush
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
                                # because next iteration from n + 1, it will not count current node in the next loop

        # add steps in the visited
        for nod in graph:
            # the value is the step number to visit the node
            visited = {}
            dfs(nod, 0)

        return degree

n = 7
edge = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]

assert Solution().minTrioDegree(n, edge) == 0