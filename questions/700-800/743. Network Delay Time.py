
import math
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        # minimum first search
        # only search the minimum search time
        node_neighbour = defaultdict(list)

        for u, v, w in times:
            node_neighbour[u].append((v, w))

        total_node_times = {k: 0}
        max_step = 0
        current_node = [k]

        while current_node:
            for _ in range(len(current_node)):
                node = current_node.pop(0)
                # find all the node starting from node
                for vi, wi in node_neighbour[node]:
                    if total_node_times.get(vi, math.inf) > total_node_times.get(node) + wi:
                        total_node_times[vi] = total_node_times[node] + wi
                        current_node.append(vi)

        if len(total_node_times) < n:
            return -1
        else:
            return max(total_node_times.values())

assert Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,4]],3, 1) == 3