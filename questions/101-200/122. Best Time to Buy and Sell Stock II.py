

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # find the loca minimum and local maximum

        index = 0
        profit = 0

        while index < len(prices) - 1:
            # find the local minimum
            while index < len(prices) - 1 and prices[index] > prices[index + 1]:
                index += 1
            put = prices[index]
            # find the local maxmium
            while index < len(prices) - 1 and prices[index] < prices[index + 1]:
                index += 1

            call = prices[index]
            # call index is higher than put index
            profit += call - put

        return profit
