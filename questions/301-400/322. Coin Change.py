


class Solution:
    def coinChange(self, coins, amount: int) -> int:

        if amount <= 0:
            return 0
        sorted_coins = sorted(coins, reverse=True)  # reverse the denominations, think about
        # tips, using the coins from largest denominations
        ans = []

        def find_fewer_coins(coins, amount, tmp):
            nonlocal ans
            if amount == 0 and not ans:
                ans = list(tmp)
                return True
            elif amount < 0:
                return False
            else:
                for coin in coins:
                    tmp.append(coin)
                    if find_fewer_coins(coins, amount - coin, tmp):
                        return True
                    tmp.pop(-1)
                return False

        find_fewer_coins(sorted_coins, amount, [])

        if ans:
            return len(ans)
        else:
            return -1


assert Solution().coinChange([1,2,5], 11) == 3
assert Solution().coinChange([2], 3) == -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1