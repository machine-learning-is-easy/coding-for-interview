

class Solution:
    def uniquePathsIII(self, grid) -> int:
        ROW, COL = len(grid), len(grid[0])
        start, end = (), ()
        path = 2
        # find start square , end square and squares to walk over
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    path += 1

        visited = set()

        def dfs(start, end, curpath):
            # check if square is visited or obstacle
            if start in visited or grid[start[0]][start[1]] == -1:
                return 0
            # check if destination is reached and all nodes are visited
            if start == end:
                if curpath == path:
                    return 1
                else:
                    return 0

            count = 0
            # add square to visited
            visited.add(start)
            # 4-directional walks
            for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                if 0 <= (x + start[0]) < ROW and 0 <= (y + start[1]) < COL:
                    # increment count
                    count += dfs((x + start[0], y + start[1]), end, curpath + 1)
                    # remove square from visited
            visited.remove(start)
            return count

        return dfs(start, end, 1)


class Solution:
    def uniquePathsIII(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        # find the starting points
        starting = None
        empty_cell = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    starting = (i, j)
                elif grid[i][j] == 0:
                    empty_cell += 1

        if starting == None:
            return -1
        sur = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, remain):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == -1:
                return 0
            if grid[r][c] == 2:
                return 1 if remain == 0 else 0

            grid[r][c] = -1
            count = 0
            for dr, dc in sur:
                new_r, new_c = r + dr, c + dc
                count += dfs(new_r, new_c, remain - 1)
            grid[r][c] = 0
            return count

        return dfs(starting[0], starting[1], empty_cell + 1) # +1 for the end point steps

grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
assert Solution().uniquePathsIII(grid) == 4