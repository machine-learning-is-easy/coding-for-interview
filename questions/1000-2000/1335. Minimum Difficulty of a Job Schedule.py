

def minDifficulty(jobDifficulty, d: int) -> int:
    n = len(jobDifficulty)
    if n < d: return -1
    dp = [[float('inf')] * n + [0] for _ in range(d + 1)]
    for d in range(1, d + 1):
        for i in range(n - d + 1):
            maxd = 0
            for j in range(i, n - d + 1):
                maxd = max(maxd, jobDifficulty[j])
                dp[d][i] = min(dp[d][i], maxd + dp[d - 1][j + 1])
    return dp[d][0]
# the time complexity is O(n^2 * d) and the space complexity is O(n * d)


from functools import lru_cache
import math
class Solution:
    def minDifficulty(self, jobs, d: int) -> int:
        @lru_cache()
        def dfs(i, d):
            if len(jobs) - i < d: return float('inf')
            if d == 0:
                if i < len(jobs):
                    return float('inf')
                else:
                    return 0
            curmax = float('-inf')
            res = float('inf')
            for j in range(i, len(jobs)):
                curmax = max(curmax, jobs[j])
                res = min(res, curmax + dfs(j + 1, d - 1))
            return res

        res = dfs(0, d)
        return res if res != math.inf else -1

# time complexity is O(n^2 * d) and the space complexity is O(n * d)
# explain  why the complexity is O(n^2 * d)
# the reason is that we have n * d states, and for each state, we have to iterate through n elements to find the maximum element.
# so the time complexity is O(n^2 * d) and the space complexity is O(n * d)

