

class Solution:
    def shortestDistance(self, grid) -> int:
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        total_distance = [[0] * n for _ in range(m)]
        reachable_count = [[0] * n for _ in range(m)]
        buildings = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        num_buildings = len(buildings)

        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # BFS from each building
        for bx, by in buildings:
            queue = deque([(bx, by, 0)])
            visited = [[False] * n for _ in range(m)]
            visited[bx][by] = True

            while queue:
                x, y, dist = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                        visited[nx][ny] = True
                        total_distance[nx][ny] += dist + 1
                        reachable_count[nx][ny] += 1
                        queue.append((nx, ny, dist + 1))

        # Find the minimum distance for land reachable by all buildings
        min_distance = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reachable_count[i][j] == num_buildings:
                    min_distance = min(min_distance, total_distance[i][j])

        return min_distance if min_distance != float('inf') else -1

# Time complexity: O(m^2 * n^2)
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        row_n = len(grid)
        col_n = len(grid[0])
        distance = [[0] * col_n for _ in range(row_n)]
        connection = [[0] * col_n for _ in range(row_n)]

        buildings = [(i, j) for i in range(row_n) for j in range(col_n) if grid[i][j] == 1]
        len_b = len(buildings)
        sur = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i, j in buildings:
            # BFS searching from i, j
            queue = [(i, j, 0)]
            d = 0
            visited = set()
            visited.add((i, j))
            while queue:
                r, c, cur_step = queue.pop(0)
                for dr, dc in sur:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < row_n and 0 <= new_c < col_n and (new_r, new_c) not in visited:
                        if grid[new_r][new_c] == 0:
                            queue.append((new_r, new_c, cur_step + 1))
                            distance[new_r][new_c] += cur_step + 1
                            connection[new_r][new_c] += 1
                            visited.add((new_r, new_c))
        min_distance = math.inf
        for i in range(row_n):
            for j in range(col_n):
                if connection[i][j] == len_b:
                    min_distance = min(min_distance, distance[i][j])
        return min_distance if min_distance != math.inf else -1

grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
assert Solution().shortestDistance(grid) == 7