
"""
questions: can the elements be 0, negative?
if 0 is allowed, the max_so_far = max(current, max_so_far * current, min_so_far * current)
if 0 is not allowed, the max_so_far = max(max_so_far * current, min_so_far * current)

is negative is allowed, the max_so_far = max(current, max_so_far * current, min_so_far * current)
if no negative elements, the max_so_far = max(current, max_so_far * current)
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            current = nums[i]
            max_tmp = max(current, max_so_far * current, min_so_far * current)
            min_so_far = min(current, max_so_far * current, min_so_far * current)

            max_so_far = max_tmp

            result = max(max_so_far, result)
        return result