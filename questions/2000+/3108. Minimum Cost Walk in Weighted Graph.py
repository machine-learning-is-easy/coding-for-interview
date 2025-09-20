

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def bfs(node):
            # get all linked nodes:
            visited = set([node])
            queue = [node]
            bitwise = -1
            while queue:
                n = queue.pop(0)
                for nxt, w in graph[n]:
                    if nxt not in visited:
                        queue.append(nxt)
                        visited.add(nxt)
                        bitwise = bitwise & w
                    else:
                        bitwise = bitwise & w # if already visited, need to do bitwise AND, possible from different edge

            return visited, bitwise
        # save the result for later different node but the same group
        groupid = 1
        global_visited = set()
        group_dict = dict()
        value_dict = defaultdict(int)
        for node in graph.keys():
            if node not in global_visited:
                nodes, value = bfs(node)
                global_visited.update(nodes)
                group_dict[groupid] = nodes
                value_dict[groupid] = value
            groupid += 1

        res = []
        for s, e in query:
            for key in group_dict:
                if s in group_dict[key] and e in group_dict[key]:
                    res.append(value_dict[key])
                    break
            else:
                res.append(-1)

        return res