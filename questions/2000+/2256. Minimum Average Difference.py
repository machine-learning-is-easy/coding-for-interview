
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        sum_right = sum(nums)
        len_right = len(nums)
        sum_left = 0
        len_left = 0

        min_avg = inf
        index = 0

        for i in range(len(nums)):

            sum_left += nums[i]
            len_left += 1

            sum_right -= nums[i]
            len_right -= 1

            # in case of only zeroes left on right
            if sum_right == 0:
                v = sum_left // len_left
            else:
                v = abs(
                    sum_left // len_left - sum_right // len_right
                )

            if v < min_avg:
                min_avg = v
                index = i

        return index