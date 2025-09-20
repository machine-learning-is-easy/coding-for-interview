
# DFS version
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        m = len(flights)
        for i in range(m):
            u, v, w = flights[i]
            adj[u].append((v, w))

        @lru_cache(None)
        def dp(u, k):
            if u == dst: return 0
            if k == 0: return math.inf
            ans = math.inf
            for v, w in adj[u]:
                ans = min(ans, w+dp(v, k-1))
            return ans

        ans = dp(src, k+1)
        return ans if ans != math.inf else -1


# BFS version
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for s,e,p in flights:
            graph[s][e] = p
        cost = [math.inf for _ in range(n)]
        q = deque([[src, 0]])
        for _ in range(k+1):
            size = len(q)
            for _ in range(size):
                [ele, curCost] = q.popleft()
                for nextNode in graph[ele]:
                    nextNodePrice = curCost+graph[ele][nextNode]
                    if nextNodePrice<cost[nextNode]:
                        cost[nextNode] = nextNodePrice
                        q.append([nextNode, nextNodePrice])
        if cost[dst]==math.inf:
            return -1
        return cost[dst]


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        # Build the graph
        for u, v, cost in flights:
            graph[u].append((v, cost))

        # Min-heap: (total_cost, current_city, stops_used)
        heap = [(0, src, 0)]

        # Best prices to reach a city with a given number of stops
        best = dict()

        while heap:
            cost, city, stops = heapq.heappop(heap)

            if city == dst:
                return cost

            if stops > k:
                continue

            # Avoid visiting worse (higher cost) or deeper (too many stops) paths
            if (city, stops) in best and best[(city, stops)] <= cost:
                continue

            best[(city, stops)] = cost

            for nei, price in graph[city]:
                heapq.heappush(heap, (cost + price, nei, stops + 1))

        return -1