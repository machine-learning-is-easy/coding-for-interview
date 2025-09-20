

# can we buy and sell the stock at the same day
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left minimum right maximum

        left_min = [0] * len(prices)

        ind = 0
        min_left = float("inf")
        while ind < len(prices):
            min_left = min(prices[ind], min_left)
            left_min[ind] = min_left
            ind += 1

        right_max = [0] * len(prices)
        ind = len(prices) - 1
        max_right = 0

        while ind >= 0:
            max_right = max(prices[ind], max_right)
            right_max[ind] = max_right
            ind -= 1

        max_profit = 0

        ind = 0
        while ind < len(prices) - 1:
            max_profit = max(right_max[ind] - left_min[ind], max_profit)
            ind += 1

        return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update min price
            profit = price - min_price  # Calculate profit
            max_profit = max(max_profit, profit)  # Update max profit

        return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min = float('inf')
        max_profit = 0

        for price in prices:
            max_profit = max(price - left_min, max_profit)
            left_min = min(price, left_min)

        return max_profit