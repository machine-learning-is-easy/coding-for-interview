
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(start, shape, i, j):
            if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]) and grid[i][j] == 1:
                shape.append((i-start[0], j-start[1])) # track shape using starting coords
                grid[i][j] = 0 # make sure we don't visit again
                dfs(start,shape,i+1,j)
                dfs(start,shape,i-1,j)
                dfs(start,shape,i,j+1)
                dfs(start,shape,i,j-1)
            return shape
        unique_islands, islands = set(), 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = tuple(dfs((i,j), [], i, j)) # shape of island we just visited
                    if island not in unique_islands:
                        unique_islands.add(island)
                        islands += 1
        return islands