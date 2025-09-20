


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = set()
        # converted to a graph
        graph = defaultdict(list)

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for n in graph[node]:
                dfs(n)

        section = 0
        for nod in range(n):
            if nod not in visited:
                dfs(nod)
                section += 1

        return section