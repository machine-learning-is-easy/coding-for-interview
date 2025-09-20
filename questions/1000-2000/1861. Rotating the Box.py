

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])

        # Step 1: Rotate the grid 90 degrees clockwise
        # rotated_grid = [[boxGrid[m - 1 - i][j] for i in range(m)] for j in range(n)]
        rotated_grid = [[0] * m for _ in range(n)]
        for new_r in range(n):
            for new_c in range(m):
                old_c = new_r
                old_r = m - 1 - new_c
                rotated_grid[new_r][new_c] = boxGrid[old_r][old_c]

        # Step 2: Apply gravity to each column of the rotated grid
        for j in range(m):
            # We will work with the current column 'j' of the rotated grid
            # Extract the column, ignore obstacles, and accumulate stones
            count = 0
            for i in range(n - 1, -1, -1):
                if rotated_grid[i][j] == "*":
                    count = 0
                elif rotated_grid[i][j] == ".":
                    count += 1
                elif rotated_grid[i][j] == "#":
                    rotated_grid[i][j], rotated_grid[i + count][j] = rotated_grid[i + count][j], rotated_grid[i][j]

        # Step 3: Return the final rid after rotation and gravity simulation
        return rotated_grid