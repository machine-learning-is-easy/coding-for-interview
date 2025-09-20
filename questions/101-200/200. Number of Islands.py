
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # make the connection to the existing cell to 0

        def part_of_island(i, j, grid):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'

            part_of_island(i, j + 1, grid)
            part_of_island(i, j - 1, grid)
            part_of_island(i + 1, j, grid)
            part_of_island(i - 1, j, grid)

            # loop over entire grid, if found 1, set the number of islands +1

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    part_of_island(i, j, grid)
        # if found one island, set the other neighours to 0

        return islands