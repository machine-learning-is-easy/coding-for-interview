

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        # Copy the last row as the initial dp state
        dp = triangle[-1][:]

        # Start from the second last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[row])):
                # Update dp[i] with the min path sum of the two adjacent numbers in the row below
                dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])

        # The top element contains the result
        return dp[0]

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        n = len(triangle)

        @lru_cache(maxsize=None)
        def dfs(row: int, col: int) -> int:
            # Base case: if we're at the last row
            if row == n - 1:
                return triangle[row][col]

            # Recursive case: choose the minimum path from the two possible children
            down_left = dfs(row + 1, col)
            down_right = dfs(row + 1, col + 1)

            return triangle[row][col] + min(down_left, down_right)

        return dfs(0, 0)