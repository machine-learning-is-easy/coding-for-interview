

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])

        def dfs(r, c):
            if 0 <= r < row and 0 <= c < col:
                if grid[r][c] == 0:
                    return 0
                else:
                    area = 1
                    grid[r][c] = 0
                    for neig in [(r, c + 1), (r, c - 1), (r - 1, c), (r + 1, c)]:
                        area += dfs(neig[0], neig[1])
                    return area
            else:
                return 0

        max_area = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area