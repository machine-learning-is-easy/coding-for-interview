
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(list)
        for node1, node2 in connections:
            graph[node1].append(node2), graph[node2].append(node1)

        arrival_time = [None] * n
        critical_connections = []

        def dfs(node=0, parent=-1, time=1):
            # First section, call DFS and assign the value of arrival time
            if arrival_time[node]: return  # only keep the original arrival time.
            arrival_time[node] = time
            for neighbour in graph[node]:
                if neighbour == parent: continue
                dfs(neighbour, node, time + 1)
                # the second section
                # all the linked neighboour arrvial time assigned, from the deepest arrival time, check belows
                if arrival_time[neighbour] == time + 1:
                    # when before entering the DFS, it is empty, but call neighour, not encounter a loop in neighbour nodes and all the nodes connecting to neighbour
                    critical_connections.append((node, neighbour))
                else:
                    # if find a loop, It is due to DFS feature, the first loop node is the previous visited node.
                    # all the loop depth will be assigned the same depth which is the first node of loop
                    arrival_time[node] = min(arrival_time[node], arrival_time[neighbour])

        dfs()
        return critical_connections


connections = [[0,1],[1,2],[2,0],[1,3]]
assert Solution().criticalConnections(4, connections) == [[1,3]]
