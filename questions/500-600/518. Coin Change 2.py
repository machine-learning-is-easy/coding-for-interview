

class Solution:
    def change(self, amount: int, coins) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1  # one coin, 0 amount

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[- 1]


assert Solution().change(5, [1, 2, 5]) == 4


'''
Now the strategy is here:

Add coins one-by-one, starting from base case "no coins".

For each added coin, compute recursively the number of combinations for each amount of money from 0 to amount.

Algorithm

Initiate number of combinations array with the base case "no coins": dp[0] = 1, and all the rest = 0.

Loop over all coins:

For each coin, loop over all amounts from 0 to amount:

For each amount x, compute the number of combinations: dp[x] += dp[x - coin].
Return dp[amount].
'''