
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        total = 0
        left = 0
        min_len = len(nums) + 1
        for ind in range(len(nums)):
            total += nums[ind]
            while total >= target:
                min_len = min(min_len, ind - left + 1)
                total -= nums[left]
                left += 1
        if min_len == len(nums) + 1:
            return 0
        return min_len