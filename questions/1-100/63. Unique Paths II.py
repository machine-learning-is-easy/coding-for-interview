


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0] * cols for _ in range(rows)]

        dp[0][0] = 1
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        for _ in range(1, rows):
            if obstacleGrid[_ - 1][0] != 1:
                dp[_][0] = 1
            else:
                break

        for _ in range(1, cols):
            if obstacleGrid[0][_ - 1] != 1:
                dp[0][_] = 1
            else:
                break

        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j - 1] != 1 and obstacleGrid[i - 1][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                elif obstacleGrid[i][j - 1] != 1:
                    dp[i][j] = dp[i][j - 1]
                elif obstacleGrid[i - 1][j] != 1:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]