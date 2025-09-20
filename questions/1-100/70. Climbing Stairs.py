

class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 2:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for ind in range(3, n + 1):
            dp[ind] = dp[ind - 1] + dp[ind - 2]

        return dp[-1]