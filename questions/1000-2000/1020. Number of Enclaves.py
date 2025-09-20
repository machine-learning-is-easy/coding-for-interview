
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n, ans = len(grid), len(grid[0]), 0

        def move(i, j, grid):
            if (i < 0 or j < 0 or i >= m or j >= n):
                return False, 0
            elif (grid[i][j] == 0):
                return True, 0
            grid[i][j] = 0
            a = move(i - 1, j, grid)
            b = move(i + 1, j, grid)
            c = move(i, j - 1, grid)
            d = move(i, j + 1, grid)
            return a[0] and b[0] and c[0] and d[0], 1 + a[1] + b[1] + c[1] + d[1]

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1):
                    valid, count = move(i, j, grid)
                    if (valid):
                        ans += count

        return ans