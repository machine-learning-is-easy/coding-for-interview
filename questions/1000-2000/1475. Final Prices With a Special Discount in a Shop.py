
class Solution:
    def finalPrices(self, prices):

        res = [0] * len(prices)
        stack = []
        for ind, num in enumerate(prices):
            while stack and num < prices[stack[-1]]:
                pre_ind = stack.pop(-1)
                res[pre_ind] = num
            stack.append(ind)
        return res


prices = [8,4,6,2,3]
assert Solution().finalPrices(prices) == [4,2,4,2,3]