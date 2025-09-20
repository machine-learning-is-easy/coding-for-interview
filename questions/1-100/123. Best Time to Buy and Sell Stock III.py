

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to track max profit
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for price in prices:
            # First buy: try to buy at lowest price
            buy1 = max(buy1, -price)
            # First sell: sell after first buy
            sell1 = max(sell1, buy1 + price)
            # Second buy: buy again after selling once
            buy2 = max(buy2, sell1 - price)
            # Second sell: sell second time
            sell2 = max(sell2, buy2 + price)

        return sell2