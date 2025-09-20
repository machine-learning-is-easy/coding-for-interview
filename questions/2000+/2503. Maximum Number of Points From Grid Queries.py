


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        row = len(grid)
        col = len(grid[0])
        sorted_query = [(val, ind) for ind, val in enumerate(queries)]
        sorted_query.sort()
        sur = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        queue = [(grid[0][0], 0, 0)]
        result = [0] * len(queries)
        visited = set([(0, 0)])
        count = 0
        for ind in range(len(sorted_query)):
            val, i = sorted_query[ind]
            while queue[0][0] < val:
                cur_v, r, c = heapq.heappop(queue)
                if cur_v < val:
                    count += 1
                for dr, dc in sur:
                    new_r = r + dr
                    new_c = c + dc
                    if 0 <= new_r < row and 0 <= new_c < col and (new_r, new_c) not in visited:
                        heapq.heappush(queue, (grid[new_r][new_c], new_r, new_c))
                        visited.add((new_r, new_c))

            result[i] = count
        return result