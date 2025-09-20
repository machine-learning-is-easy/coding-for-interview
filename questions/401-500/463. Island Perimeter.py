

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        columns = len(grid[0])
        # depth first search grid
        # find the first element which is 1

        perimeter = 0
        neighbours = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    for delta_r, delta_c in neighbours:
                        new_r = r + delta_r
                        new_c = c + delta_c
                        if new_r >= 0 and new_r < rows and new_c >= 0 and new_c < columns:
                            if grid[new_r][new_c] == 0:
                                perimeter += 1
                        else:
                            perimeter += 1
        return perimeter

# another option is dfs.
# find a 1 and dfs until find a 0.

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        queue = []
        n = len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    queue.append((i, j))
                    visited.add((i, j))
                    while queue:
                        r, c = queue.pop(0)
                        for dr, dc in directions:
                            new_r, new_c = r+dr, c + dc
                            if new_r < 0 or new_c < 0 or new_r >= len(grid) or new_c >= len(grid[0]):
                                count += 1
                            elif (new_r, new_c) not in visited and grid[new_r][new_c] == '1':
                                queue.append((new_r, new_c))
                                visited.add((new_r, new_c))
                            elif grid[new_r][new_c] == '0':
                                count += 1
        return count

