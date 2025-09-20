
# k can be more than m * n times

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        rows = len(grid)
        cols = len(grid[0])

        def one_shift(grid):
            for row_ind in range(rows):
                last_elment = grid[row_ind].pop()
                grid[row_ind].insert(0, last_elment)

            ans = grid[-1][0]
            for row_ind in range(rows - 2, -1, -1):
                if row_ind + 1 < rows:
                    grid[row_ind + 1][0] = grid[row_ind][0]

            grid[0][0] = ans

        for _ in range(k% (rows * cols)):
            one_shift(grid)

        return grid