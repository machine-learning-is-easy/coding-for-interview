

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for r1 in range(rows):
            for r2 in range(r1 + 1, rows):
                shared_ones = 0
                for c in range(cols):
                    if grid[r1][c] == 1 and grid[r2][c] == 1:
                        shared_ones += 1
                if shared_ones >= 2:
                    count += shared_ones * (shared_ones - 1) // 2

        return count