

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])

        start = [-1, -1]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    start = [i, j]
                elif grid[i][j] in "abcdef":
                    count += 1

        queue = [(start[0], start[1], "")]
        visited = set([(start[0], start[1], "")])
        res = 0

        while queue:
            for _ in range(len(queue)):
                x, y, keys = queue.pop(0)
                if len(keys) == count:
                    return res

                for new_x, new_y in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] != "#":
                        if grid[new_x][new_y] in "ABCDEF":
                            if grid[new_x][new_y].lower() not in keys:
                                continue
                        if grid[new_x][new_y] in "abcdef" and grid[new_x][new_y] not in keys:
                            tmp = keys + grid[new_x][new_y]
                        else:
                            tmp = keys

                        if (new_x, new_y, tmp) not in visited:
                            queue.append((new_x, new_y, tmp))
                            visited.add((new_x, new_y, tmp))
            res += 1

        return -1

grid = ["@..aA","..B#.","....b"]

assert Solution().shortestPathAllKeys(grid) == 6