
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        modulo = 1000000007

        for dice_left in range(1, n + 1):
            for target_left in range(1, target + 1):
                for i in range(1, min(k, target_left) + 1):
                    dp[dice_left][target_left] += dp[dice_left - 1][target_left - i]
                dp[dice_left][target_left] %= modulo
        return dp[n][target]

# similar dfs
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        res = 0
        memo = []
        def recursive(amount, n, k):
            nonlocal res
            nonlocal memo
            if amount == 0 and n == 0:
                res += 1
            elif amount < 0 or n < 0:
                return

            for amt in range(1, k + 1):
                memo.append(amt)
                recursive(amount - amt, n - 1, k)
                memo.pop()

        recursive(target, n, k)
        return res

assert Solution().numRollsToTarget(1,6,3) == 1

assert Solution().numRollsToTarget(2, 6, 7) == 6