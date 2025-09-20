

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

# think the logic change if it is possible to reach the destination

# n = 5
# edge = [[0,1],[0,2],[0,3],[0,3],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# start = 0
# end = 4
#
# assert Solution().leadsToDestination(n, edge, start, end) == True

n = 4
edge = [[0,1],[1,2],[2,3],[0,3]]
start = 0
end = 3
assert Solution().leadsToDestination(n, edge, start, end) == True