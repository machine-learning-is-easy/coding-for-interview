

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # 1. build graph
        graph = collections.defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        # 2. dfs
        visited = set([0])
        for nextNode in graph[0]:
            if not self.dfs(graph, visited, 0, nextNode):
                return False
        return len(visited) == n

    def dfs(self, graph, visited, prevNode, node):
        if node in visited:
            return False
        visited.add(node)

        for nextNode in graph[node]:
            if nextNode != prevNode:
                if not self.dfs(graph, visited, node, nextNode):
                    return False
        return True

