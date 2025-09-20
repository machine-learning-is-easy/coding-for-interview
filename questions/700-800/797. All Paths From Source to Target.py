
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dag = defaultdict(list)

        for start, end in enumerate(graph):
            dag[start] = end

        all_path = []

        def dfs(node, target, tmp):
            nonlocal all_path
            if node == target:
                all_path.append(list(tmp))
            nonlocal visited
            visited.add(node)
            if node in dag:
                for nei in dag[node]:
                    if nei not in visited:
                        tmp.append(nei)
                        dfs(nei, target, tmp)
                        tmp.remove(nei)

            visited.remove(node)
            return

        visited = set()
        dfs(0, len(graph) - 1, [0])
        return all_path