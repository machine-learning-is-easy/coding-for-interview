

class Solution:
    def lengthOfLongestSubsequence(self, nums, target: int) -> int:

        dp = [-1] * (target + 1)
        dp[0] = 0
        for n in nums:
            for i in range(target - n, -1, -1):
                if dp[i] >= 0:
                    dp[i + n] = max(dp[i + n], dp[i] + 1)
        return dp[target]

nums = [1,2,3,4,5]

assert Solution().lengthOfLongestSubsequence(nums, target=9) == 3