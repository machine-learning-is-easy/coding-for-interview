
class Solution:
    def combinationSum4(self, nums, target):
        memo = {} # only the elments of nums can be repeated selected. if not repeated, could not use memo

        def combine(nums,target,memo):
            if target==0:
                return 1
            if target < 0:
                return 0
            res=0
            if target in memo:
                return memo[target]

            for item in nums:
                a = combine(nums, target-item, memo)
                res += a

            memo[target]=res
            return res

        return combine(nums, target, memo)

assert Solution().combinationSum4([1, 2, 3], target=4) == 7


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]
