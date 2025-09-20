
from collections import deque

class Solution:
    def containsCycle(self, grid) -> bool:
        visited = set()
        stack = deque()

        row_n = len(grid)
        col_n = len(grid[0])

        for row, row_g in enumerate(grid):
            for col, val in enumerate(row_g):
                if (row, col) not in visited:   # if new cell
                    # add to stack current cell and previous cell
                    # we don't have previous cell, so replace it to -1, -1
                    stack.append([row, col])
                    while stack:
                        r, c = stack.pop()
                        if (r, c) in visited:
                            return True   # we saw this cell before -> cycle,
                        visited.add((r, c))  # add current cell to the stack

                        for d_r, d_c in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                            # we exclude previous cell from addition to stack
                            if 0 <= r + d_r < row_n and (r + d_r, c + d_c) not in visited and \
                               0 <= c + d_c < col_n and grid[r + d_r][c + d_c] == val:
                                # make sure the added cell is not visited, the spreading is moving forward
                                # if two path joins at a cell, when the two path spread, it able to add the same
                                # cell to the stack.
                                    stack.append([r + d_r, c + d_c])
        return False


grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]

assert Solution().containsCycle(grid) == True