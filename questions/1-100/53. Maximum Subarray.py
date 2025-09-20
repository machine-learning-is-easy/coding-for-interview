

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # really simple
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0: # previous accumulative sum is negative, will start new
                nums[i] += nums[i - 1]
            max_sum = max(nums[i], max_sum)

        return max_sum