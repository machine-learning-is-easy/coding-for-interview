

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # Initialize DP arrays
        cash = [0] * n
        hold = [0] * n

        # Base case
        cash[0] = 0
        hold[0] = -prices[0]

        # Fill the arrays
        for i in range(1, n):
            cash[i] = max(cash[i-1], hold[i-1] + prices[i] - fee)
            hold[i] = max(hold[i-1], cash[i-1] - prices[i])

        return cash[-1]



class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        cash = 0
        hold = -prices[0]

        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)

        return cash