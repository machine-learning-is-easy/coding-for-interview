

class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        # breath first search
        if not grid:
            return -1

        r = len(grid)
        c = len(grid[0])

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        visited = set()

        starts = [(0, 0)]

        adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]

        steps = 1
        if (r - 1, c - 1) in starts:
            return steps
        while starts:
            steps += 1
            for _ in range(len(starts)):
                cell = starts.pop(0)
                # travers the points at starts
                for adj in adjacent:
                    i = cell[0] + adj[0]
                    j = cell[1] + adj[1]
                    if (i, j) == (r - 1, c - 1):
                        return steps
                    else:
                        if i >= 0 and i < r and j >= 0 and j < c:
                            if grid[i][j] == 0:
                                if (i, j) not in visited:
                                    visited.add((i, j))
                                    starts.append((i, j))
        return -1


assert Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]) == 4
assert Solution().shortestPathBinaryMatrix([[0]]) == 1