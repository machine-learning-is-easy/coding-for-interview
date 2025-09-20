

class Solution:
    def maxScore(self, nums: List[int]) -> int:

        @cache
        def dp(nums):
            if len(nums) == 2:
                total = math.gcd(nums[0], nums[1])
            else:
                total = 0
                for i in range(len(nums)):
                    for j in range(i + 1, len(nums)):
                        temp = dp((nums[i], nums[j])) * len(nums) // 2
                        temp += dp(nums[:i] + nums[i + 1:j] + nums[j + 1:])
                        total = max(total, temp)

            return total

        return dp(tuple(nums))