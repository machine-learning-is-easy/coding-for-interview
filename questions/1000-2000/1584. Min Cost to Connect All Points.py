
import collections
import heapq
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n, c = len(points), collections.defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                d = manhattan(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))
        cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
        visited[0] = 1
        heapq.heapify(heap)
        while heap:
            d, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt+1, ans+d
                for record in c[j]: heapq.heappush(heap, record)
            if cnt >= n: break
        return ans



class Solution(object):
    def minCostConnectPoints(self, points):
        def distance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        n = len(points)
        dist = collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                i_j_distance = distance(points[i], points[j])
                dist[i].append((i_j_distance, j))
                dist[j].append((i_j_distance, i))

        ans = 0
        heap = dist[0]
        heapq.heapify(heap)
        visited = set([0])
        while heap:
            distance, point = heapq.heappop(heap)
            ans += distance
            visited.add(point)
            if len(visited) == n:
                break
            for d, p in dist[point]:
                if p not in visited:
                    heapq.heappush(heap, (d, p))
        return ans

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
assert Solution().minCostConnectPoints(points) == 20