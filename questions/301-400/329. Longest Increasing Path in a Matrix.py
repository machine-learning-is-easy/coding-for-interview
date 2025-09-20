

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # *************
        rows = len(matrix)
        if rows < 1: return 0
        cols = len(matrix[0])
        if cols < 1: return 0

        dp = [[0] * cols for r in range(rows)]

        maxPath = 0
        nodes = []
        for r in range(rows):
            for c in range(cols):
                nodes.append((matrix[r][c],r,c))

        nodes.sort(key=lambda x: x[0], reverse=True)

        for v,r,c in nodes:
            maxBigger = 0
            if r < rows - 1 and matrix[r + 1][c] > v: maxBigger = max(maxBigger, dp[r + 1][c])
            if r > 0 and matrix[r - 1][c] > v: maxBigger = max(maxBigger, dp[r - 1][c])
            if c > 0 and matrix[r][c - 1] > v: maxBigger = max(maxBigger, dp[r][c - 1])
            if c < cols - 1 and matrix[r][c + 1] > v: maxBigger = max(maxBigger, dp[r][c + 1])

            dp[r][c] = 1 + maxBigger
            maxPath = max(maxPath, dp[r][c])
        return maxPath



# dfs version
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix:
            return 0

        suround = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        row = len(matrix)
        col = len(matrix[0])

        @cache  # lru_cache will timeout
        def dfs(r, c):
            max_path = 1
            for dr, dc in suround:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < row and 0 <= new_c < col and matrix[new_r][new_c] > matrix[r][c]:
                    max_path = max(dfs(new_r, new_c) + 1, max_path)

            return max_path

        final_max_path = 0
        for r in range(row):
            for c in range(col):
                final_max_path = max(final_max_path, dfs(r, c))
        return final_max_path

# // Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the matrix.
# // Space Complexity: O(m * n) due to memoization and recursion stack.

# without cache
# Time Complexity without Memoization: O(m^2 * n^2)
# Space Complexity without Memoization: O(m * n) (mainly due to recursion stack).