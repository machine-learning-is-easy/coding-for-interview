

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        new_grid = [x for row in grid for x in row]
        new_grid.sort()
        median = 0
        if(len(new_grid)%2 == 0):
            median = new_grid[(len(new_grid)//2)-1]
        else:
            median = new_grid[len(new_grid)//2]
        result = [abs(elem - median) for elem in new_grid]
        for i in result:
            if(i%x != 0):
                return -1
        return sum(result)//x