

from collections import defaultdict


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        num_counts = defaultdict(int)
        for num in nums:
            num_counts[num] += 1

        largest_outlier = float('-inf')
        for num in num_counts.keys():
            potential_outlier = total_sum - 2 * num
            if potential_outlier in num_counts:
                if potential_outlier != num or num_counts[num] > 1: # in order to avoid the same number.
                    largest_outlier = max(largest_outlier, potential_outlier)
        return largest_outlier


nums = [2,3,5,10]
assert Solution().getLargestOutlier(nums) == 10

nums = [-2,-1,-3,-6,4]
assert Solution().getLargestOutlier(nums) == 4

nums = [1,1,1,1,1,5,5]
assert Solution().getLargestOutlier(nums) == 5
