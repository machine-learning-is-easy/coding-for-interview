

# time out version
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        neighhour = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        max_value = float("-inf")

        def dfs(r, c, min_value):
            nonlocal max_value
            if r == row - 1 and c == col - 1:
                max_value = max(max_value, min_value)
                return

            for dr, dc in neighhour:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < row and 0 <= new_c < col and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    dfs(new_r, new_c, min(grid[new_r][new_c], min_value))
                    visited.remove((new_r, new_c))

        dfs(0, 0, grid[0][0])
        return max_value


# optimize version

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:

        dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        R, C = len(grid), len(grid[0])

        maxHeap = [(-grid[0][0], 0, 0)]
        seen = [[0 for _ in range(C)] for _ in range(R)]
        while maxHeap:
            val, x, y = heapq.heappop(maxHeap)
            # seen[x][y] = 1 # got TLE
            if x == R - 1 and y == C - 1: return -val
            for dx, dy in dire:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and not seen[nx][ny]:
                    seen[nx][ny] = 1  # passed
                    heapq.heappush(maxHeap, (max(val, -grid[nx][ny]), nx, ny))
        return -1