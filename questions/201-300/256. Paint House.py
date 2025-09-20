

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        n = len(costs)
        dp = [costs[0]]  # initialize with the first row

        for i in range(1, n):
            red = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
            blue = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
            green = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
            dp.append([red, blue, green])

        return min(dp[-1])