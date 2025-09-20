
import math
class Solution:
    def minCost(self, nums, costs) -> int:
        n = len(nums)
        ng, nl, dp = []*n,[]*n, [math.inf]*n
        dp[0] = 0
        for i in range(n):
            while ng and nums[ng[-1]] <= nums[i]:
                # repeating check the element in the monotonic stack, it makes sure all the element are lower or equal than the
                # first element in the stack. if it can not pop all the element in the stack, it will end up with pop
                # intermediate element, the cost will be inf. only one can reach the first element can have a value.
                dp[i] = min(dp[i], dp[ng.pop()] + costs[i])
            while nl and nums[nl[-1]] > nums[i]:
                dp[i] = min(dp[i], dp[nl.pop()] + costs[i])
            ng.append(i)
            nl.append(i)
        return dp[n-1]

nums = [3, 2, 4, 4, 1]
costs = [3, 7, 6, 4, 2]

assert Solution().minCost(nums, costs) == 8
